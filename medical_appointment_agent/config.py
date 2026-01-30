"""
Configuration and database for medical appointment system.
"""

DOCTORS_DB = {
    "Cardiology": ["Dr. Patel", "Dr. Lee"],
    "Neurology": ["Dr. Jones", "Dr. Wang"]
}

APPOINTMENT_SLOTS = {
    "Dr. Patel": ["Jan 21 9AM", "Jan 22 2PM"],
    "Dr. Lee": ["Jan 20 10AM", "Jan 22 1PM"],
    "Dr. Jones": ["Jan 23 11AM", "Jan 24 3PM"],
    "Dr. Wang": ["Jan 21 2PM", "Jan 23 10AM"]
}

SPECIALTY_MAP = {
    "cardiology": "Cardiology",
    "cardiologist": "Cardiology",
    "cardiologists": "Cardiology",
    "neurology": "Neurology",
    "neurologist": "Neurology",
    "neurologists": "Neurology",
    "dermatology": "Dermatology",
    "dermatologist": "Dermatology",
    "dermatologists": "Dermatology",
}