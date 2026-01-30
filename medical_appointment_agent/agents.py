"""
Agent configurations for task-oriented and goal-oriented approaches.
"""

from langchain_core.prompts import PromptTemplate
from langchain.agents import AgentExecutor, create_react_agent
from .tools import get_all_tools

# Task-oriented template
TASK_TEMPLATE = """You are a helpful assistant that completes one specific task at a time.

You have access to the following tools:

{tools}

Use this exact format:

Question: the input question
Thought: think about what to do
Action: one of [{tool_names}]
Action Input: the plain input value
Observation: the tool result
Thought: I have the answer
Final Answer: state the result

RULES:
- Action Input must be plain text (examples: "Cardiology", "Dr. Patel", "Dr. Patel for Jan 21 9AM")
- After getting ONE Observation, immediately give Final Answer
- Final Answer should just state what the Observation shows

Question: {input}
Thought:{agent_scratchpad}"""

# Goal-oriented template
GOAL_TEMPLATE = """You are a medical appointment assistant. Help users achieve their goals by using tools in sequence.

You have access to the following tools:

{tools}

Use this format:

Question: the user's goal
Thought: think about the next step
Action: one of [{tool_names}]
Action Input: plain value only
Observation: tool result
... (repeat as needed)
Thought: goal is complete
Final Answer: summary

IMPORTANT:
- Action Input must be plain text (e.g., "Cardiology", "Dr. Patel", "Dr. Patel for Jan 21 9AM")
- DO NOT repeat failed actions - try something different or give up
- If a tool returns an ERROR, check what went wrong before retrying
- After 2-3 attempts at the same action, move on or report failure

Question: {input}
Thought:{agent_scratchpad}"""

def create_task_oriented_agent(llm):
    """Create a task-oriented agent executor."""
    tools = get_all_tools()
    prompt = PromptTemplate.from_template(TASK_TEMPLATE)
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    
    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=2,
        handle_parsing_errors=True,
        early_stopping_method="force",
        return_intermediate_steps=False
    )

def create_goal_oriented_agent(llm):
    """Create a goal-oriented agent executor."""
    tools = get_all_tools()
    prompt = PromptTemplate.from_template(GOAL_TEMPLATE)
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    
    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=15,
        handle_parsing_errors=True,
        early_stopping_method="force",
        return_intermediate_steps=False
    )