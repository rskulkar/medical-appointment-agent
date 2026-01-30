"""
LangChain tools for medical appointment booking.
"""

from langchain.tools import tool
from .config import DOCTORS_DB, APPOINTMENT_SLOTS, SPECIALTY_MAP
from .utils import clean_tool_input, get_all_doctors

@tool
def FindDoctorsTool(specialty: str) -> str:
    """Return available doctors for the given specialty."""
    specialty_clean = clean_tool_input(specialty)
    
    import re
    match = re.search(r'([A-Za-z]+)', specialty_clean)
    if match:
        specialty_clean = match.group(1)
    
    key = SPECIALTY_MAP.get(specialty_clean.lower())
    
    if not key:
        return f"ERROR: Specialty '{specialty_clean}' not found. Available specialties: Cardiology, Neurology."
    
    doctors = DOCTORS_DB.get(key, [])
    if not doctors:
        return f"ERROR: No doctors found for specialty: {key}"
    
    return f"Available doctors in {key}: {', '.join(doctors)}"

@tool
def CheckAvailabilityTool(doctor_name: str) -> str:
    """Get available appointment slots for the selected doctor."""
    doctor_clean = clean_tool_input(doctor_name)
    
    all_doctors = get_all_doctors()
    if doctor_clean not in all_doctors:
        return f"ERROR: Doctor '{doctor_clean}' not found. Available doctors: {', '.join(all_doctors)}"
    
    slots = APPOINTMENT_SLOTS.get(doctor_clean, [])
    
    if not slots:
        return f"ERROR: No available slots found for {doctor_clean}"
    
    return f"Available slots for {doctor_clean}: {', '.join(slots)}"

@tool
def BookAppointmentTool(doctor_and_time: str) -> str:
    """Book an appointment."""
    booking_info = clean_tool_input(doctor_and_time)
    return f"✅ Appointment booked: {booking_info}"

def get_all_tools():
    """Return list of all available tools."""
    return [FindDoctorsTool, CheckAvailabilityTool, BookAppointmentTool]