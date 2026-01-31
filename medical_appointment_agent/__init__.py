"""
Medical Appointment Agent - A LangChain-based appointment booking system.
"""

from .agents import create_task_oriented_agent, create_goal_oriented_agent
from .workflows import run_task_oriented_workflow
from .tools import get_all_tools
from .config import DOCTORS_DB, APPOINTMENT_SLOTS, SPECIALTY_MAP
from .llm_factory import (
    create_llm_with_fallback,
    get_rate_limit_safe_llm,
    RateLimitError,
)


__version__ = "0.1.0"

__all__ = [
    "create_task_oriented_agent",
    "create_goal_oriented_agent",
    "run_task_oriented_workflow",
    "get_all_tools",
    "DOCTORS_DB",
    "APPOINTMENT_SLOTS",
    "SPECIALTY_MAP",
    "create_llm_with_fallback",
    "get_rate_limit_safe_llm",
    "RateLimitError",
]