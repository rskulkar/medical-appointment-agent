# Medical Appointment Agent

A LangChain-based intelligent agent system for medical appointment booking with both task-oriented and goal-oriented approaches.

## Features

- **Task-Oriented Workflow**: Step-by-step orchestrated appointment booking
- **Goal-Oriented Workflow**: Autonomous multi-step planning from high-level goals
- **Flexible LLM Support**: Works with Google Gemini, OpenAI, Anthropic, or local models
- **Robust Error Handling**: Graceful failure management at each step
- **Extensible Architecture**: Easy to add new specialties, doctors, or tools

## Installation

### From PyPI (once published)
```bash
pip install medical-appointment-agent
```

### From source
```bash
git clone https://github.com/rskulkar/medical-appointment-agent.git
cd medical-appointment-agent
pip install -e .
```

### For development
```bash
pip install -e ".[dev]"
```

## Quick Start

### Task-Oriented Approach
```python
from medical_appointment_agent import create_task_oriented_agent, run_task_oriented_workflow
from langchain_google_genai import ChatGoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "your-api-key"
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)

agent = create_task_oriented_agent(llm)
result = run_task_oriented_workflow(agent, "cardiologists")
print(result)
```

### Goal-Oriented Approach
```python
from medical_appointment_agent import create_goal_oriented_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "your-api-key"
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)

agent = create_goal_oriented_agent(llm)
response = agent.invoke({"input": "Book me an appointment with a cardiologist"})
print(response['output'])
```

## Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=medical_appointment_agent

# Run specific test file
pytest tests/test_tools.py

# Run with verbose output
pytest -v
```

## Configuration

You can customize the available doctors and specialties by modifying `config.py`:
```python
DOCTORS_DB = {
    "Cardiology": ["Dr. Patel", "Dr. Lee"],
    "Neurology": ["Dr. Jones", "Dr. Wang"],
    # Add more specialties...
}
```

## License

MIT License

## Contributing

Pull requests are welcome! Please make sure to update tests as appropriate.