"""
Unit tests for agent creation.
"""

import pytest
from unittest.mock import Mock
from medical_appointment_agent.agents import (
    create_task_oriented_agent,
    create_goal_oriented_agent,
    TASK_TEMPLATE,
    GOAL_TEMPLATE
)

class TestAgentCreation:
    """Tests for agent creation functions."""
    
    def test_create_task_oriented_agent(self):
        """Test that task-oriented agent is created successfully."""
        mock_llm = Mock()
        agent = create_task_oriented_agent(mock_llm)
        
        assert agent is not None
        assert hasattr(agent, 'invoke')
        assert agent.max_iterations == 2
        assert agent.handle_parsing_errors == True
    
    def test_create_goal_oriented_agent(self):
        """Test that goal-oriented agent is created successfully."""
        mock_llm = Mock()
        agent = create_goal_oriented_agent(mock_llm)
        
        assert agent is not None
        assert hasattr(agent, 'invoke')
        assert agent.max_iterations == 15
        assert agent.handle_parsing_errors == True
    
    def test_task_template_contains_rules(self):
        """Test that task template contains important rules."""
        assert "Action Input" in TASK_TEMPLATE
        assert "plain text" in TASK_TEMPLATE.lower()
        assert "Final Answer" in TASK_TEMPLATE
    
    def test_goal_template_contains_rules(self):
        """Test that goal template contains important rules."""
        assert "Action Input" in GOAL_TEMPLATE
        assert "DO NOT repeat failed actions" in GOAL_TEMPLATE
        assert "Final Answer" in GOAL_TEMPLATE