import os
import requests

CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY", "YOUR_CLAUDE_API_KEY")
CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"

def call_claude(prompt):
    headers = {
        "x-api-key": CLAUDE_API_KEY,
        "content-type": "application/json"
    }
    payload = {
        "model": "claude-3-opus-20240229",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 2048
    }
    # Uncomment for real API usage
    # resp = requests.post(CLAUDE_API_URL, json=payload, headers=headers)
    # return resp.json()["content"]
    return "Claude LLM Output (mocked)"  # Replace with real Claude call

def suggest_eda(meta, data_path):
    prompt = f"Given this Kaggle competition: {meta}, and data at {data_path}, suggest EDA steps in Python code."
    return call_claude(prompt)

def suggest_model(meta, eda_steps):
    prompt = f"Given this metadata: {meta} and EDA steps: {eda_steps}, suggest Python code for a baseline model and data pipeline."
    return call_claude(prompt)

def improve_code(prev_code, last_score):
    prompt = f"Given this previous model code:\n{prev_code}\n and achieved score {last_score}, suggest improved model code for the next iteration."
    return call_claude(prompt)