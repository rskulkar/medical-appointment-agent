"""Unit tests for workflows."""

import pytest
from unittest.mock import Mock, MagicMock
from medical_appointment_agent.workflows import run_task_oriented_workflow

class TestTaskOrientedWorkflow:
    """Tests for task-oriented workflow."""
    
    def test_successful_workflow(self, capsys):
        """Test a successful end-to-end workflow."""
        # Mock agent executor
        mock_executor = Mock()
        
        # Mock responses for each step
        mock_executor.invoke.side_effect = [
            {"output": "Available doctors in Cardiology: Dr. Patel, Dr. Lee"},
            {"output": "Available slots for Dr. Patel: Jan 21 9AM, Jan 22 2PM"},
            {"output": "✅ Appointment booked: Dr. Patel for Jan 21 9AM"}
        ]
        
        result = run_task_oriented_workflow(mock_executor, "cardiologists")
        
        assert result["success"] == True
        assert result["specialty"] == "cardiologists"
        assert result["doctor"] == "Dr. Patel"
        assert result["time_slot"] == "Jan 21 9AM"
        assert result["error"] is None
        
        # Verify agent was called 3 times (find, check, book)
        assert mock_executor.invoke.call_count == 3
    
    def test_workflow_fails_at_step1(self, capsys):
        """Test workflow stops when no doctors are found."""
        mock_executor = Mock()
        mock_executor.invoke.return_value = {
            "output": "ERROR: Specialty 'dermatologists' not found."
        }
        
        result = run_task_oriented_workflow(mock_executor, "dermatologists")
        
        assert result["success"] == False
        assert result["error"] == "No doctors found"
        assert result["doctor"] is None
        assert result["time_slot"] is None
        
        # Verify agent was only called once (find)
        assert mock_executor.invoke.call_count == 1
    
    def test_workflow_fails_at_step2(self, capsys):
        """Test workflow stops when no slots are available."""
        mock_executor = Mock()
        mock_executor.invoke.side_effect = [
            {"output": "Available doctors in Cardiology: Dr. Patel, Dr. Lee"},
            {"output": "ERROR: No available slots found for Dr. Patel"}
        ]
        
        result = run_task_oriented_workflow(mock_executor, "cardiologists")
        
        assert result["success"] == False
        assert result["error"] == "No available slots"
        assert result["doctor"] == "Dr. Patel"
        assert result["time_slot"] is None
        
        # Verify agent was called twice (find, check)
        assert mock_executor.invoke.call_count == 2
    
    def test_workflow_fails_at_step3(self, capsys):
        """Test workflow when booking fails."""
        mock_executor = Mock()
        mock_executor.invoke.side_effect = [
            {"output": "Available doctors in Cardiology: Dr. Patel, Dr. Lee"},
            {"output": "Available slots for Dr. Patel: Jan 21 9AM, Jan 22 2PM"},
            {"output": "Booking failed due to system error"}
        ]
        
        result = run_task_oriented_workflow(mock_executor, "cardiologists")
        
        assert result["success"] == False
        assert result["error"] == "Booking failed"
        assert result["doctor"] == "Dr. Patel"
        assert result["time_slot"] == "Jan 21 9AM"
        
        # Verify agent was called 3 times
        assert mock_executor.invoke.call_count == 3