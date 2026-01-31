"""
LLM factory with automatic rate limit handling and model fallback.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from google.api_core import exceptions
import time
from .config import DEFAULT_MODEL, DEFAULT_TEMPERATURE, FALLBACK_MODELS

__all__ = ["create_llm_with_fallback", "get_rate_limit_safe_llm", "RateLimitError"]

class RateLimitError(Exception):
    """Raised when all models are rate limited."""
    pass

def create_llm_with_fallback(
    model=None,
    temperature=DEFAULT_TEMPERATURE,
    api_key=None,
    verbose=True
):
    """
    Create an LLM with automatic fallback to alternative models if rate limited.
    
    Args:
        model: Primary model to use (defaults to DEFAULT_MODEL)
        temperature: Temperature setting for the model
        api_key: Google API key (optional, uses env var if not provided)
        verbose: Whether to print model selection info
    
    Returns:
        ChatGoogleGenerativeAI instance
    """
    models_to_try = [model or DEFAULT_MODEL] + [
        m for m in FALLBACK_MODELS if m != (model or DEFAULT_MODEL)
    ]
    
    for i, model_name in enumerate(models_to_try):
        try:
            if verbose:
                if i == 0:
                    print(f"🤖 Initializing LLM with model: {model_name}")
                else:
                    print(f"🔄 Trying fallback model: {model_name}")
            
            llm_kwargs = {
                "model": model_name,
                "temperature": temperature,
            }
            
            if api_key:
                llm_kwargs["google_api_key"] = api_key
            
            llm = ChatGoogleGenerativeAI(**llm_kwargs)
            
            # Test the model with a simple call
            test_response = llm.invoke("test")
            
            if verbose:
                print(f"✅ Successfully initialized with {model_name}")
            
            return llm
            
        except exceptions.ResourceExhausted as e:
            if verbose:
                print(f"⚠️  Rate limit hit for {model_name}")
            
            if i == len(models_to_try) - 1:
                # All models exhausted
                raise RateLimitError(
                    f"All models are rate limited. Please wait and try again. "
                    f"Tried models: {', '.join(models_to_try)}"
                )
            
            # Wait a bit before trying next model
            time.sleep(2)
            continue
            
        except Exception as e:
            if verbose:
                print(f"❌ Error with {model_name}: {str(e)}")
            
            if i == len(models_to_try) - 1:
                raise
            
            continue
    
    raise Exception("Failed to initialize any model")


def get_rate_limit_safe_llm(api_key=None, verbose=True):
    """
    Convenience function to get a rate-limit-safe LLM.
    
    Args:
        api_key: Google API key
        verbose: Whether to print status messages
    
    Returns:
        ChatGoogleGenerativeAI instance with fallback support
    """
    return create_llm_with_fallback(api_key=api_key, verbose=verbose)