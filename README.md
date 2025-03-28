# Smolagents Demo Project

This project demonstrates the usage of Smolagents, a minimalist AI agent framework developed by Hugging Face.

## Setup

1. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Hugging Face API token:
```
HUGGINGFACE_API_TOKEN=your_token_here
```

## Project Structure

- `requirements.txt`: Project dependencies
- `example.py`: Basic example of using Smolagents
- `smol_agents.ipynb`: Interactive Jupyter notebook with multiple examples
- `.env`: Environment variables (create this file)

## Usage

### Running the Python Script
```bash
python3 example.py
```

### Running the Jupyter Notebook
```bash
jupyter notebook
```
Then open `smol_agents.ipynb` in your browser.

The notebook contains three examples:
1. Calculator Function: Creates a function for basic arithmetic operations
2. List Operations: Demonstrates various list manipulations (duplicates, second largest, rotation)
3. String Manipulation: Shows advanced string operations (word reversal, palindrome checking, title case)

## Resources

- [Smolagents Documentation](https://smolagents.org/)
- [Hugging Face Hub](https://huggingface.co/) 