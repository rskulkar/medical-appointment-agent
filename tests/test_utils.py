"""Unit tests for utility functions."""

import pytest
from medical_appointment_agent.utils import (
    extract_doctors_from_text,
    extract_time_slots_from_text,
    get_all_doctors,
    clean_tool_input
)

class TestExtractDoctors:
    """Tests for extract_doctors_from_text function."""
    
    def test_extract_single_doctor(self):
        text = "Available doctors: Dr. Patel"
        result = extract_doctors_from_text(text)
        assert result == ["Dr. Patel"]
    
    def test_extract_multiple_doctors(self):
        text = "Available doctors: Dr. Patel, Dr. Lee"
        result = extract_doctors_from_text(text)
        assert set(result) == {"Dr. Patel", "Dr. Lee"}
    
    def test_extract_no_doctors(self):
        text = "No doctors available"
        result = extract_doctors_from_text(text)
        assert result == []
    
    def test_extract_doctors_with_noise(self):
        text = "In Cardiology, we have Dr. Patel and Dr. Lee available."
        result = extract_doctors_from_text(text)
        assert set(result) == {"Dr. Patel", "Dr. Lee"}
    
    def test_extract_duplicates_removed(self):
        text = "Dr. Patel, Dr. Lee, Dr. Patel"
        result = extract_doctors_from_text(text)
        assert len(result) == 2
        assert set(result) == {"Dr. Patel", "Dr. Lee"}


class TestExtractTimeSlots:
    """Tests for extract_time_slots_from_text function."""
    
    def test_extract_single_slot(self):
        text = "Available: Jan 21 9AM"
        result = extract_time_slots_from_text(text)
        assert result == ["Jan 21 9AM"]
    
    def test_extract_multiple_slots(self):
        text = "Available: Jan 21 9AM, Jan 22 2PM"
        result = extract_time_slots_from_text(text)
        assert set(result) == {"Jan 21 9AM", "Jan 22 2PM"}
    
    def test_extract_no_slots(self):
        text = "No slots available"
        result = extract_time_slots_from_text(text)
        assert result == []
    
    def test_extract_slots_different_months(self):
        text = "Available: Jan 21 9AM, Feb 15 3PM, Dec 31 11AM"
        result = extract_time_slots_from_text(text)
        assert len(result) == 3


class TestGetAllDoctors:
    """Tests for get_all_doctors function."""
    
    def test_get_all_doctors(self):
        result = get_all_doctors()
        assert "Dr. Patel" in result
        assert "Dr. Lee" in result
        assert "Dr. Jones" in result
        assert "Dr. Wang" in result
        assert len(result) == 4


class TestCleanToolInput:
    """Tests for clean_tool_input function."""
    
    def test_clean_basic_input(self):
        assert clean_tool_input("Cardiology") == "Cardiology"
    
    def test_remove_parameter_name(self):
        assert clean_tool_input("specialty=Cardiology") == "Cardiology"
    
    def test_remove_quotes(self):
        assert clean_tool_input('"Cardiology"') == "Cardiology"
        assert clean_tool_input("'Cardiology'") == "Cardiology"
    
    def test_remove_parameter_and_quotes(self):
        assert clean_tool_input('specialty="Cardiology"') == "Cardiology"
    
    def test_fix_doctor_name_missing_period(self):
        assert clean_tool_input("Dr Patel") == "Dr. Patel"
    
    def test_fix_doctor_name_with_parameter(self):
        assert clean_tool_input('doctor="Dr Patel"') == "Dr. Patel"
    
    def test_whitespace_handling(self):
        assert clean_tool_input("  Cardiology  ") == "Cardiology"