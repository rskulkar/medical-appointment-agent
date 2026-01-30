"""Pytest configuration and fixtures."""

import pytest

@pytest.fixture
def mock_llm():
    """Fixture providing a mock LLM for testing."""
    from unittest.mock import Mock
    return Mock()