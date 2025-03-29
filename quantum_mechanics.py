import os
from dotenv import load_dotenv
from smolagents import CodeAgent, HfApiModel
from smolagents.models import TransformersModel
from typing import List, Dict, Any

def format_chat_message(role: str, content: str) -> Dict[str, Any]:
    """Format a chat message in the correct structure for the model.
    
    Args:
        role: The role of the message sender (e.g., "user" or "assistant")
        content: The actual message content
        
    Returns:
        A properly formatted message dictionary
    """
    return {
        "role": role,
        "content": [{"type": "text", "text": content}]
    }

def print_chat(messages: List[Dict[str, Any]]) -> None:
    """Print chat messages in a nice format.
    
    Args:
        messages: List of message dictionaries
    """
    for msg in messages:
        role = msg["role"].upper()
        content = msg["content"][0]["text"]
        print(f"\n{role}:")
        print("-" * (len(role) + 1))
        # Print content with proper newline handling
        print(str(content).rstrip())  # Convert to string and remove trailing whitespace
        print()

# Load environment variables
load_dotenv()

def main():
    model = TransformersModel(model_id="HuggingFaceTB/SmolLM-135M-Instruct",
                              max_new_tokens=5000)

    # Create messages using the helper function
    messages = [
        format_chat_message("user", "Explain quantum mechanics in simple terms.")
    ]
    
    # Print the conversation so far
    print_chat(messages)
    
    # Get and print the response
    response = model(messages, stop_sequences=["END"])
    print_chat([{"role": response.role, "content": [{"type": "text", "text": str(response.content)}] }])


if __name__ == "__main__":
    main() 