# Build-Your-Own AI Agent Framework

## 📌 Project Overview
This project implements a **custom AI Agent Framework built from scratch using Python**, without using any pre-made agent orchestration tools such as **n8n, LangChain Agents, AutoGPT, or CrewAI**.

The goal of this project is to demonstrate a **first-principles implementation of an AI agent**, focusing on agent architecture rather than relying on black-box tools.

---

## 🎯 Problem Statement (Intel Unnati)
> Build your own AI Agent Framework without using premade tools like n8n.

---

## ✅ Why This Solution Works
This project satisfies the problem statement because:

- ❌ No agent orchestration tools are used (n8n, LangChain agents, etc.)
- ✅ The agent loop is implemented manually
- ✅ Decision-making, memory, and tool execution are custom-built
- ✅ The framework is modular, extensible, and explainable
- ✅ LLM usage is optional and replaceable (LLM-agnostic design)

The intelligence lies in the **agent architecture**, not in external libraries.

---

## 🧠 AI Agent Architecture

The agent follows the standard AI agent lifecycle:

Perception → Reasoning → Action → Memory → Repeat

markdown
Copy code

### Workflow:
1. The agent **perceives** user input
2. A **planner module** decides the appropriate action
3. The agent **executes tools or language responses**
4. Results are stored in **memory**
5. The loop continues autonomously

---

## 📁 Project Directory Structure

ai-agent-framework/
│
├── main.py # Entry point of the agent
│
└── agent/
├── init.py # Package initializer
├── agent.py # Core AI agent logic
├── planner.py # Decision-making / planning module
├── memory.py # Short-term and long-term memory
├── tools.py # Tool definitions (calculator, search)
└── llm.py # LLM abstraction (API or stub)

yaml
Copy code

---

## 📂 File Descriptions

### `main.py`
- Starts the AI agent
- Runs the autonomous interaction loop

---

### `agent/agent.py`
- Core implementation of the AI agent
- Implements:
  - Perception
  - Reasoning
  - Action
  - Memory update
- Prints reasoning logs for transparency

---

### `agent/planner.py`
- Decides **what action the agent should take**
- Routes input to:
  - Calculator tool
  - Search tool
  - LLM response
- Provides explainable reasoning

---

### `agent/memory.py`
- Stores:
  - Short-term memory (recent inputs)
  - Long-term memory (responses and outcomes)
- Enables inspection using the `memory` command

---

### `agent/tools.py`
- Defines tools the agent can use
- Current tools:
  - Calculator
  - Search (mock implementation)
- Easily extensible for new tools

---

### `agent/llm.py`
- Language Model abstraction layer
- Supports:
  - OpenAI API (if available)
  - Local stub fallback (no API / quota safe)
- Ensures robustness and fault tolerance

---

## 🔧 Features Implemented

- Autonomous agent loop
- Explainable decision-making
- Tool-augmented reasoning
- Memory management
- Graceful fallback when LLM API is unavailable
- Modular and extensible design

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ai-agent-framework.git
cd ai-agent-framework
2️⃣ Run the agent
bash
Copy code
python main.py
3️⃣ Example interaction
vbnet
Copy code
User: 10+5
[Reasoning] Detected mathematical expression, using calculator tool
Agent: 15
🛠️ Future Enhancements (Planned)
This framework is designed to evolve over time. Planned improvements include:

Multi-step task planning

Context-aware memory usage

Vector-based memory (embeddings)

LLM-based tool selection

Additional tools (file handling, APIs)

Goal completion tracking

📚 Conclusion
This project demonstrates how an AI Agent Framework can be built from scratch, focusing on architecture, transparency, and extensibility. It fulfills the Intel Unnati problem statement by avoiding premade agent tools and implementing all agent components manually.

👤 Author
Avinash Raj
B.Tech IT Student
Intel Unnati Program Participant
