"""
Example of using the goal-oriented approach.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
import os
from getpass import getpass

from medical_appointment_agent import create_goal_oriented_agent

# Setup
api_key = getpass("Enter your Google API Key: ")
os.environ["GOOGLE_API_KEY"] = api_key

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)
agent = create_goal_oriented_agent(llm)

# Single goal request
response = agent.invoke({
    "input": "Book me an appointment with a cardiologist"
})
print("\n📋 FINAL RESULT:", response['output'])