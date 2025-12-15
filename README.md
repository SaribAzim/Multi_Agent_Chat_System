# Multi-Agent Chat System

## Overview
This project implements a **multi-agent chat system** where a **Coordinator (Manager) agent** orchestrates three specialized worker agents:

1. **ResearchAgent** – Retrieves information from a pre-defined knowledge base.
2. **AnalysisAgent** – Performs comparisons, reasoning, and simple calculations on retrieved data.
3. **MemoryAgent** – Stores structured knowledge, maintains conversation context, and allows retrieval via keyword/vector search.

The system demonstrates **role separation, inter-agent coordination, structured memory, and adaptive decision-making**.

---

## Architecture & Sequence Flow
1. **User Query** → sent to **Coordinator**
2. Coordinator **extracts topic** and decides which agent(s) to invoke:
   - Simple information → ResearchAgent  
   - Comparative/analytical tasks → ResearchAgent → AnalysisAgent  
   - Retrieval of past discussion → MemoryAgent
3. Coordinator **aggregates responses** and updates **MemoryAgent**.
4. Response sent back to user.

Optional sequence diagram:

User → Coordinator → ResearchAgent → AnalysisAgent → Coordinator → MemoryAgent → Coordinator → User

How to Run
1. Install Requirements
pip install -r requirements.txt

2. Run Main Program
python main.py

3. Run Tests (Generates Outputs)
python -m tests.run_tests


Output files are saved in the outputs/ folder:
simple_query.txt
complex_query.txt
memory_test.txt
multi_step.txt
collaborative.txt

Memory Design
Structured storage: Each record has:
timestamp, topic, content, source, agent, confidence

Memory types:
Conversation memory – full history of interactions
Knowledge base – persistent facts
Agent state memory – tracks what each agent learned
Search & retrieval: Keyword/topic search and vector similarity to avoid redundant work
Adaptive Behavior & Decision-Making
Coordinator analyzes query complexity and sequences agent calls.

Implements fallback behavior if no data is found or topic is unrecognized:
"Sorry, I could not identify a topic to research."
Memory retrieval avoids repeating previous work.
Analysis agent provides simple confidence scoring in outputs.

Containerization
Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

docker-compose.yaml (optional)
version: '3.8'
services:
  multi-agent:
    build: .
    container_name: multi_agent_chat
    volumes:
      - .:/app
    tty: true


Build & run with:

docker-compose build
docker-compose up

Outputs
The outputs/ folder contains sample console outputs for five scenarios:
simple_query.txt – basic information retrieval
complex_query.txt – research + analysis
memory_test.txt – retrieval of previous discussion
multi_step.txt – multi-step queries (research → analysis)
collaborative.txt – multiple queries in a single session demonstrating collaboration between agents
