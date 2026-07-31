from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv 


load_dotenv() #this loads the environment variables from the .env file, including the LLM API key.

@tool
def calculator(a: float, b: float, operation: str) -> float  :
    """A simple calculator tool that performs basic arithmetic operations. Format: calculator(a, b, operation)"""
    print("Tool has been called")
    if operation == "add" or operation == "plus":
        return a + b
    elif operation == "subtract" or operation == "minus":
        return a - b
    elif operation == "multiply" or operation == "times":
        return a * b
    elif operation == "divide" or operation == "over":
        return a / b if b != 0 else float('inf')
print("\n")

def main():
    model = "Placeholder for your model"  # Replace with your actual model initialization
    
    tools = [calculator]  
    agent_executor = create_agent(model, tools)
    
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    print("You can ask questions or give commands to the AI.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input == "exit":
            print("Exiting the AI Chatbot. Goodbye!")
            break
        print("\nAI: ", end="", flush=True) 
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            for node_name, data in chunk.items():
                if "messages" in data:

                    print(data["messages"][-1].content, end="", flush=True)
        print() # Print a newline at the end of the stream

if __name__ == "__main__":
    main()