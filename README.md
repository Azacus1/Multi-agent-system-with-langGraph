# Multi-Agent Workflow with LangChain and LangGraph

This project demonstrates a **collaborative multi-agent system** using `LangChain` and `LangGraph`. It is designed to process user queries by leveraging two specialized AI agents: a **Research Agent** and a **Writer Agent**. Each agent performs a distinct role and collaborates to generate high-quality answers.

---

## Key Features

1. **Dynamic Multi-Agent Collaboration**:
   - The **Research Agent** fetches relevant information based on the user's query.
   - The **Writer Agent** synthesizes the research results into a concise and well-structured summary.

2. **Role-Specific Prompts**:
   - Tailored prompts ensure that each agent performs its role effectively using `ChatPromptTemplate`.

3. **Workflow Orchestration**:
   - Built using `langgraph.graph.StateGraph` to manage the execution order and interaction between agents.

4. **Modular Design**:
   - Each agent's functionality is encapsulated, making the system easy to extend or modify.

5. **Simple Execution**:
   - A single function, `run_multi_agent_system`, handles the user query and executes the workflow seamlessly.

---

## How It Works

### Workflow
1. **Input**:
   - The user provides a query, such as a topic or question they need information about.

2. **Agent Tasks**:
   - **Research Agent**: Gathers detailed information related to the query.
   - **Writer Agent**: Summarizes the research results into a concise and polished format.

3. **Output**:
   - The final output is a user-friendly summary of the research results.

### Example Query
For example, the query:
> "What are the key challenges in AI-based electricity theft detection?"

Results in:
1. The **Research Agent** fetching detailed insights.
2. The **Writer Agent** summarizing those insights into a clear answer.

---

## Technology Stack

- **LangChain**:
  - Provides prompt management and integration with OpenAI models.
- **LangGraph**:
  - Manages the multi-agent workflow using a state graph.
- **OpenAI API**:
  - Powers the agents using GPT-3.5-turbo.

---

## Installation

### Prerequisites
- Python 3.8 or later
- OpenAI API key

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-openai-api-key"  # On Windows: set OPENAI_API_KEY="your-openai-api-key"
   ```

---

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Enter your query when prompted:
   ```
   Enter your query: What are the key benefits of AI in healthcare?
   ```

3. View the final summarized answer:
   ```
   Final answer: AI in healthcare offers benefits like personalized treatments, early disease detection, and enhanced diagnostic accuracy.
   ```

---

## Code Overview

### Core Components

1. **Agents**:
   - **Research Agent**: Gathers information based on the query.
   - **Writer Agent**: Summarizes the gathered information into a user-friendly answer.

2. **Workflow Management**:
   - Built using `StateGraph` to define and orchestrate the multi-agent flow.

### Key Functions

- **research_agent_func**:
  Fetches detailed information using the research prompt.

- **writer_agent_func**:
  Summarizes the research results into a concise format.

- **run_multi_agent_system(query)**:
  Executes the workflow for a given query and returns the final answer.

---

## Future Enhancements

- Add more specialized agents, such as:
  - **Validator Agent** to verify the accuracy of research.
  - **Editor Agent** to improve grammar and style.
- Expand the system to handle multi-query workflows.
- Integrate with external knowledge bases for enhanced research capabilities.

---


## Contact

For any questions or collaboration opportunities, feel free to reach out:

- **Email**: aman_srivastava14@outlook.com
- **LinkedIn**: [Aman Srivastava](https://www.linkedin.com/in/aman-srivastava-5b1068153/)
- **GitHub**: [Azacus1](https://github.com/InfiniteLoopster-coder/)

