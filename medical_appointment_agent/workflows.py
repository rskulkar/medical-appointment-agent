"""
Workflow orchestration for task-oriented approach.
"""

from .utils import extract_doctors_from_text, extract_time_slots_from_text

def run_task_oriented_workflow(agent_executor, specialty):
    """
    Run the complete task-oriented workflow: Find → Check → Book
    
    Args:
        agent_executor: The LangChain agent executor
        specialty: The medical specialty to search for (e.g., "cardiologists")
    
    Returns:
        dict: Results containing success status and details
    """
    result = {
        "success": False,
        "specialty": specialty,
        "doctor": None,
        "time_slot": None,
        "error": None
    }
    
    print("=" * 70)
    print(f"WORKFLOW: Find {specialty} → Check Availability → Book Appointment")
    print("=" * 70)
    
    # Step 1: Find doctors
    print("\n" + "=" * 70)
    print(f"STEP 1: Find {specialty}")
    print("=" * 70)
    response1 = agent_executor.invoke({"input": f"Find {specialty}."})
    print("\n📋 OUTPUT:", response1['output'])
    
    doctors_found = extract_doctors_from_text(response1['output'])
    
    if not doctors_found or "ERROR" in response1['output']:
        result["error"] = "No doctors found"
        print("\n❌ WORKFLOW STOPPED: No doctors found. Steps 2 and 3 will not execute.")
        return result
    
    print(f"\n✅ Found {len(doctors_found)} doctor(s): {', '.join(doctors_found)}")
    selected_doctor = doctors_found[0]
    result["doctor"] = selected_doctor
    
    # Step 2: Check availability
    print("\n" + "=" * 70)
    print(f"STEP 2: Check availability for {selected_doctor}")
    print("=" * 70)
    response2 = agent_executor.invoke({"input": f"What are the available times for {selected_doctor}?"})
    print("\n📋 OUTPUT:", response2['output'])
    
    if "ERROR" in response2['output'] or "No available slots" in response2['output']:
        result["error"] = "No available slots"
        print("\n❌ WORKFLOW STOPPED: No available slots. Step 3 will not execute.")
        return result
    
    time_slots = extract_time_slots_from_text(response2['output'])
    
    if not time_slots:
        result["error"] = "Could not extract time slot"
        print("\n❌ Could not extract time slot from response.")
        return result
    
    time_slot = time_slots[0]
    result["time_slot"] = time_slot
    print(f"\n✅ Found available slot: {time_slot}")
    
    # Step 3: Book appointment
    print("\n" + "=" * 70)
    print(f"STEP 3: Book appointment with {selected_doctor} at {time_slot}")
    print("=" * 70)
    response3 = agent_executor.invoke({
        "input": f"Book {selected_doctor} for {time_slot}."
    })
    print("\n📋 OUTPUT:", response3['output'])
    
    if "✅" in response3['output'] or "booked" in response3['output'].lower():
        result["success"] = True
        print("\n✅ WORKFLOW COMPLETED SUCCESSFULLY!")
        print(f"   Doctor: {selected_doctor}")
        print(f"   Specialty: {specialty}")
        print(f"   Time: {time_slot}")
    else:
        result["error"] = "Booking failed"
        print("\n❌ BOOKING FAILED")
    
    return result