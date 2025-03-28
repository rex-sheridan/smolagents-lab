import os
from dotenv import load_dotenv
from smolagents import CodeAgent, HfApiModel

# Load environment variables
load_dotenv()

def main():
    # Initialize the agent with a Hugging Face model
    model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"
    model = HfApiModel(
        token=os.getenv("HUGGINGFACE_API_TOKEN"),
        model_id=model_id
    )
    agent = CodeAgent(
        tools=[],  # Required parameter, even if empty
        model=model, add_base_tools=True
    )

    # Example task: Create a simple calculator function
    task = """
    Create a Python function that can perform basic arithmetic operations (add, subtract, multiply, divide).
    The function should take three parameters: operation (string), num1 (float), and num2 (float).
    Return the result of the operation.
    """

    # Run the agent
    result = agent.run(task)
    print("Generated code:")
    print(result)

if __name__ == "__main__":
    main() 