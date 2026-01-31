"""
Example of using the task-oriented workflow.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
import os
from getpass import getpass

from medical_appointment_agent import create_task_oriented_agent, run_task_oriented_workflow

# Setup
api_key = getpass("Enter your Google API Key: ")
os.environ["GOOGLE_API_KEY"] = api_key

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
agent = create_task_oriented_agent(llm)

# Success case
result = run_task_oriented_workflow(agent, "cardiologists")
print(f"\nResult: {result}")

# Failure case
result = run_task_oriented_workflow(agent, "dermatologists")
print(f"\nResult: {result}")