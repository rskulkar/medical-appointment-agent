"""
Helper utility functions.
"""

import re
from .config import DOCTORS_DB

def extract_doctors_from_text(text):
    """Extract all doctor names (Dr. Lastname) from text."""
    pattern = r'Dr\.\s+[A-Z][a-z]+'
    doctors = re.findall(pattern, text)
    return list(set(doctors))

def extract_time_slots_from_text(text):
    """Extract time slots from text."""
    pattern = r'[A-Z][a-z]{2}\s+\d{1,2}\s+\d{1,2}[AP]M'
    slots = re.findall(pattern, text)
    return list(set(slots))

def get_all_doctors():
    """Get all doctors from the database."""
    all_doctors = []
    for doctors_list in DOCTORS_DB.values():
        all_doctors.extend(doctors_list)
    return all_doctors

def clean_tool_input(input_str):
    """Clean tool input by removing parameter names and extra quotes."""
    cleaned = re.sub(r'\w+=', '', input_str)
    cleaned = cleaned.strip('"').strip("'").strip()
    cleaned = re.sub(r'\bDr\s+([A-Z][a-z]+)', r'Dr. \1', cleaned)
    return cleaned