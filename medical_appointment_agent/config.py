"""Configuration and database for medical appointment system."""

# Expanded database with more specialties and doctors
DOCTORS_DB = {
    "Cardiology": ["Dr. Patel", "Dr. Lee", "Dr. Martinez", "Dr. Johnson"],
    "Neurology": ["Dr. Jones", "Dr. Wang", "Dr. Anderson", "Dr. Kim"],
    "Orthopedics": ["Dr. Brown", "Dr. Davis", "Dr. Wilson"],
    "Pediatrics": ["Dr. Taylor", "Dr. Thompson", "Dr. Garcia"],
    "Psychiatry": ["Dr. Miller", "Dr. Rodriguez", "Dr. White"],
    "Ophthalmology": ["Dr. Moore", "Dr. Martin"],
    "ENT": ["Dr. Jackson", "Dr. Lewis", "Dr. Clark"],
    "Endocrinology": ["Dr. Walker", "Dr. Hall", "Dr. Allen"],
    "Gastroenterology": ["Dr. Young", "Dr. King"],
    "Pulmonology": ["Dr. Wright", "Dr. Lopez", "Dr. Hill"],
}

# Expanded appointment slots (varied schedules)
APPOINTMENT_SLOTS = {
    # Cardiology
    "Dr. Patel": ["Jan 21 9AM", "Jan 22 2PM", "Jan 24 10AM", "Jan 25 3PM"],
    "Dr. Lee": ["Jan 20 10AM", "Jan 22 1PM", "Jan 23 9AM", "Jan 26 2PM"],
    "Dr. Martinez": ["Jan 21 11AM", "Jan 23 3PM", "Jan 24 9AM"],
    "Dr. Johnson": ["Jan 20 2PM", "Jan 22 10AM", "Jan 25 1PM", "Jan 27 11AM"],
    
    # Neurology
    "Dr. Jones": ["Jan 23 11AM", "Jan 24 3PM", "Jan 26 10AM"],
    "Dr. Wang": ["Jan 21 2PM", "Jan 23 10AM", "Jan 25 9AM", "Jan 27 2PM"],
    "Dr. Anderson": ["Jan 20 9AM", "Jan 22 3PM", "Jan 24 1PM"],
    "Dr. Kim": ["Jan 21 10AM", "Jan 23 2PM", "Jan 26 9AM"],
    
    # Orthopedics
    "Dr. Brown": ["Jan 20 11AM", "Jan 21 3PM", "Jan 23 9AM", "Jan 25 2PM"],
    "Dr. Davis": ["Jan 22 9AM", "Jan 24 2PM", "Jan 26 11AM"],
    "Dr. Wilson": ["Jan 20 1PM", "Jan 23 10AM", "Jan 25 3PM"],
    
    # Pediatrics
    "Dr. Taylor": ["Jan 21 9AM", "Jan 22 11AM", "Jan 24 2PM", "Jan 26 10AM"],
    "Dr. Thompson": ["Jan 20 10AM", "Jan 23 1PM", "Jan 25 9AM"],
    "Dr. Garcia": ["Jan 21 2PM", "Jan 24 10AM", "Jan 27 9AM"],
    
    # Psychiatry
    "Dr. Miller": ["Jan 22 10AM", "Jan 24 1PM", "Jan 26 3PM"],
    "Dr. Rodriguez": ["Jan 20 3PM", "Jan 23 11AM", "Jan 25 10AM", "Jan 27 2PM"],
    "Dr. White": ["Jan 21 1PM", "Jan 23 3PM", "Jan 26 9AM"],
    
    # Ophthalmology
    "Dr. Moore": ["Jan 20 9AM", "Jan 22 2PM", "Jan 24 11AM", "Jan 26 1PM"],
    "Dr. Martin": ["Jan 21 10AM", "Jan 23 9AM", "Jan 25 2PM"],
    
    # ENT (Ear, Nose, Throat)
    "Dr. Jackson": ["Jan 22 11AM", "Jan 24 9AM", "Jan 26 2PM"],
    "Dr. Lewis": ["Jan 20 2PM", "Jan 23 10AM", "Jan 25 11AM"],
    "Dr. Clark": ["Jan 21 9AM", "Jan 24 3PM", "Jan 27 10AM"],
    
    # Endocrinology
    "Dr. Walker": ["Jan 20 10AM", "Jan 22 1PM", "Jan 24 9AM", "Jan 26 3PM"],
    "Dr. Hall": ["Jan 21 11AM", "Jan 23 2PM", "Jan 25 10AM"],
    "Dr. Allen": ["Jan 22 9AM", "Jan 24 1PM", "Jan 27 11AM"],
    
    # Gastroenterology
    "Dr. Young": ["Jan 21 10AM", "Jan 23 1PM", "Jan 25 9AM", "Jan 27 2PM"],
    "Dr. King": ["Jan 20 11AM", "Jan 22 3PM", "Jan 24 10AM", "Jan 26 1PM"],
    
    # Pulmonology
    "Dr. Wright": ["Jan 22 10AM", "Jan 24 2PM", "Jan 26 9AM"],
    "Dr. Lopez": ["Jan 20 1PM", "Jan 23 11AM", "Jan 25 3PM", "Jan 27 10AM"],
    "Dr. Hill": ["Jan 21 9AM", "Jan 23 3PM", "Jan 25 1PM"],
}

# Expanded specialty mapping with more variants
SPECIALTY_MAP = {
    # Cardiology
    "cardiology": "Cardiology",
    "cardiologist": "Cardiology",
    "cardiologists": "Cardiology",
    "heart": "Cardiology",
    "heart doctor": "Cardiology",
    
    # Neurology
    "neurology": "Neurology",
    "neurologist": "Neurology",
    "neurologists": "Neurology",
    "brain": "Neurology",
    "nervous system": "Neurology",
    
    # Orthopedics
    "orthopedics": "Orthopedics",
    "orthopedic": "Orthopedics",
    "orthopedist": "Orthopedics",
    "bone": "Orthopedics",
    "bone doctor": "Orthopedics",
    "joint": "Orthopedics",
    
    # Pediatrics
    "pediatrics": "Pediatrics",
    "pediatric": "Pediatrics",
    "pediatrician": "Pediatrics",
    "pediatricians": "Pediatrics",
    "child doctor": "Pediatrics",
    "kids doctor": "Pediatrics",
    
    # Psychiatry
    "psychiatry": "Psychiatry",
    "psychiatric": "Psychiatry",
    "psychiatrist": "Psychiatry",
    "psychiatrists": "Psychiatry",
    "mental health": "Psychiatry",
    
    # Ophthalmology
    "ophthalmology": "Ophthalmology",
    "ophthalmologist": "Ophthalmology",
    "eye": "Ophthalmology",
    "eye doctor": "Ophthalmology",
    
    # ENT
    "ent": "ENT",
    "ear nose throat": "ENT",
    "otolaryngology": "ENT",
    "otolaryngologist": "ENT",
    
    # Endocrinology
    "endocrinology": "Endocrinology",
    "endocrinologist": "Endocrinology",
    "hormone": "Endocrinology",
    "diabetes": "Endocrinology",
    "thyroid": "Endocrinology",
    
    # Gastroenterology
    "gastroenterology": "Gastroenterology",
    "gastroenterologist": "Gastroenterology",
    "stomach": "Gastroenterology",
    "digestive": "Gastroenterology",
    "gi": "Gastroenterology",
    
    # Pulmonology
    "pulmonology": "Pulmonology",
    "pulmonologist": "Pulmonology",
    "lung": "Pulmonology",
    "lung doctor": "Pulmonology",
    "respiratory": "Pulmonology",
    
    # Not available (for testing failure cases)
    "dermatology": "Dermatology",
    "dermatologist": "Dermatology",
    "dermatologists": "Dermatology",
    "skin": "Dermatology",
    
    "urology": "Urology",
    "urologist": "Urology",
}

# LLM configuration
DEFAULT_MODEL = "gemini-2.5-flash"
DEFAULT_TEMPERATURE = 0

# Fallback models in priority order (if rate limit is hit)
FALLBACK_MODELS = [
    "gemini-2.5-flash",      # Primary - fastest, free tier
    "gemini-2.0-flash",      # Fallback 1 - older but still fast
    "gemini-flash-latest",   # Fallback 2 - alias to latest flash
    "gemini-2.5-pro",        # Fallback 3 - slower but higher quality
]
