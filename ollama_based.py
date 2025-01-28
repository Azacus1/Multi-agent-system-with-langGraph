import os
from langchain.chat_models import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from langgraph.graph import StateGraph

# Set Ollama API key
os.environ["OLLAMA_API_KEY"] = "your-ollama-api-key"

# Define roles and prompts for the agents
research_prompt = ChatPromptTemplate.from_template(
    "You are a research assistant. Find relevant information on: {query}"
)

writer_prompt = ChatPromptTemplate.from_template(
    "You are a writer. Summarize the research results into a concise answer for: {query}"
)

# Create LLM instances for each agent
research_agent = Ollama(model_name="ollama-default")
writer_agent = Ollama(model_name="ollama-default")

# Define agent functions
def research_agent_func(state):
    """
    Research agent function to find relevant information based on the query.
    """
    query = state["query"]
    response = research_agent([HumanMessage(content=research_prompt.format(query=query))])
    return {"research_result": response.content}

def writer_agent_func(state):
    """
    Writer agent function to summarize the research results into a concise answer.
    """
    query = state["query"]
    research_result = state["research_result"]
    response = writer_agent(
        [HumanMessage(content=writer_prompt.format(query=query, research_result=research_result))]
    )
    return {"final_answer": response.content}

# Build the collaborative multi-agent workflow using langGraph
workflow = StateGraph()

# Add nodes (agents) to the workflow
workflow.add_node("research_agent", research_agent_func)
workflow.add_node("writer_agent", writer_agent_func)

# Define the execution flow
workflow.set_entry_point("research_agent")
workflow.set_edge("research_agent", "writer_agent")

# Compile the workflow into an executable graph
graph = workflow.compile()

def run_multi_agent_system(query):
    """
    Run the multi-agent collaborative system for a given query.

    Args:
        query (str): The input query for the system.

    Returns:
        str: The final answer generated by the writer agent.
    """
    input_data = {"query": query}
    output_data = graph.invoke(input_data)
    return output_data["final_answer"]

# Example usage
if __name__ == "__main__":
    user_query = input("Enter your query: ")
    answer = run_multi_agent_system(user_query)
    print("\nFinal answer:", answer)
