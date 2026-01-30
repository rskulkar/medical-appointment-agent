"""
Unit tests for tools.
"""

import pytest
from medical_appointment_agent.tools import (
    FindDoctorsTool,
    CheckAvailabilityTool,
    BookAppointmentTool,
    get_all_tools
)

class TestFindDoctorsTool:
    """Tests for FindDoctorsTool."""
    
    def test_find_cardiology(self):
        result = FindDoctorsTool.invoke({"specialty": "Cardiology"})
        assert "Dr. Patel" in result
        assert "Dr. Lee" in result
        assert "ERROR" not in result
    
    def test_find_cardiology_lowercase(self):
        result = FindDoctorsTool.invoke({"specialty": "cardiology"})
        assert "Dr. Patel" in result
        assert "Dr. Lee" in result
    
    def test_find_cardiologist_variant(self):
        result = FindDoctorsTool.invoke({"specialty": "cardiologists"})
        assert "Dr. Patel" in result
        assert "Dr. Lee" in result
    
    def test_find_neurology(self):
        result = FindDoctorsTool.invoke({"specialty": "Neurology"})
        assert "Dr. Jones" in result
        assert "Dr. Wang" in result
    
    def test_find_nonexistent_specialty(self):
        result = FindDoctorsTool.invoke({"specialty": "Dermatology"})
        assert "ERROR" in result
        assert "not found" in result.lower()
    
    def test_find_with_parameter_prefix(self):
        result = FindDoctorsTool.invoke({"specialty": 'specialty="Cardiology"'})
        assert "Dr. Patel" in result
        assert "ERROR" not in result


class TestCheckAvailabilityTool:
    """Tests for CheckAvailabilityTool."""
    
    def test_check_dr_patel(self):
        result = CheckAvailabilityTool.invoke({"doctor_name": "Dr. Patel"})
        assert "Jan 21 9AM" in result
        assert "Jan 22 2PM" in result
        assert "ERROR" not in result
    
    def test_check_dr_lee(self):
        result = CheckAvailabilityTool.invoke({"doctor_name": "Dr. Lee"})
        assert "Jan 20 10AM" in result
        assert "Jan 22 1PM" in result
    
    def test_check_nonexistent_doctor(self):
        result = CheckAvailabilityTool.invoke({"doctor_name": "Dr. Smith"})
        assert "ERROR" in result
        assert "not found" in result.lower()
    
    def test_check_with_missing_period(self):
        result = CheckAvailabilityTool.invoke({"doctor_name": "Dr Patel"})
        assert "Jan 21 9AM" in result
        assert "ERROR" not in result
    
    def test_check_with_parameter_prefix(self):
        result = CheckAvailabilityTool.invoke({"doctor_name": 'doctor="Dr. Patel"'})
        assert "Jan 21 9AM" in result


class TestBookAppointmentTool:
    """Tests for BookAppointmentTool."""
    
    def test_book_appointment(self):
        result = BookAppointmentTool.invoke({
            "doctor_and_time": "Dr. Patel for Jan 21 9AM"
        })
        assert "✅" in result
        assert "Appointment booked" in result
        assert "Dr. Patel" in result
        assert "Jan 21 9AM" in result
    
    def test_book_with_parameter_prefix(self):
        result = BookAppointmentTool.invoke({
            "doctor_and_time": 'details="Dr. Patel for Jan 21 9AM"'
        })
        assert "✅" in result
        assert "Dr. Patel" in result


class TestGetAllTools:
    """Tests for get_all_tools function."""
    
    def test_get_all_tools(self):
        tools = get_all_tools()
        assert len(tools) == 3
        tool_names = [tool.name for tool in tools]
        assert "FindDoctorsTool" in tool_names
        assert "CheckAvailabilityTool" in tool_names
        assert "BookAppointmentTool" in tool_names