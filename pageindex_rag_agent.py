import os
import argparse
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from pageindex import PageIndexClient

# Load environment variables
load_dotenv()

# Initialize PageIndex Client
api_key = os.getenv("PAGEINDEX_API_KEY")
pi_client = PageIndexClient(api_key=api_key) if api_key else None

@tool
def query_document(doc_id: str, query: str) -> str:
    """
    Queries a specific document in PageIndex using its document ID and a natural language query.
    Use this tool whenever you need to find information within a specific document.
    """
    if not pi_client:
        return "Error: PageIndex API key not configured."
    
    try:
        response = pi_client.chat_completions(
            messages=[{"role": "user", "content": query}],
            doc_id=doc_id
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error querying document: {str(e)}"

@tool
def get_document_tree(doc_id: str) -> str:
    """
    Retrieves the hierarchical tree structure (table of contents) for a document.
    Useful for understanding the overall structure and sections of a document.
    """
    if not pi_client:
        return "Error: PageIndex API key not configured."
    
    try:
        tree_result = pi_client.get_tree(doc_id)
        return str(tree_result.get("result", "No tree structure found."))
    except Exception as e:
        return f"Error getting document tree: {str(e)}"

def get_agent_executor(doc_id: str):
    # Initialize LLM
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("Error: OPENAI_API_KEY not found in environment.")
        return None

    # Use a valid model name (gpt-4o)
    llm = ChatOpenAI(model="gpt-4o", openai_api_key=openai_api_key)

    # Define tools
    tools = [query_document, get_document_tree]

    # Create the expert system prompt
    system_message = (
        "You are the expert EU AI Act Chatbot. Your goal is to provide accurate, "
        "comprehensive, and easy-to-understand information about the European Union AI Act. "
        f"The user is interested in document with ID: {doc_id}. "
        "Always use this ID when calling the tools. If you need a summary or structure first, use get_document_tree. "
        "Then use query_document to find specific details to answer the user's question. "
        "Ensure your tone is professional, authoritative, and helpful."
    )
    
    # create_react_agent provides a reliable tool-calling loop
    return create_agent(model="openai:gpt-4.1", tools=tools, system_prompt=system_message)

def main():
    doc_id = os.getenv("EU_AI_ACT_DOCUMENT_ID")

    # Re-verify API key
    if not os.getenv("PAGEINDEX_API_KEY"):
        print("Error: PAGEINDEX_API_KEY not found.")
        return

    agent_executor = get_agent_executor(doc_id)
    if not agent_executor:
        return

    print(f"--- EU AI Act Chatbot for Doc ID: {doc_id} ---")
    print("Type 'exit' to quit.")

    # Use initial query if provided
    current_query = None

    while True:
        if not current_query:
            try:
                current_query = input("\nYou: ")
            except EOFError:
                break

        if current_query.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        print(f"\n--- Chatbot is thinking... ---")
        inputs = {"messages": [HumanMessage(content=current_query)]}
        
        try:
            result = agent_executor.invoke(inputs)
            final_response = result["messages"][-1].content
            print("\nChatbot:", final_response)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
        
        # Reset current_query to allow input in next iteration
        current_query = None

if __name__ == "__main__":
    main()
