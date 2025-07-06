# kaggle-agent

**A reusable, LLM-powered agent for automating Kaggle competition pipelines.**

## Features

- Downloads Kaggle competition data
- Uses Claude (or other LLM) to suggest EDA steps and baseline models
- Generates and executes Jupyter notebooks
- Supports agentic iteration (automatically tries to improve score)
- Modular and ready for CLI, API, or integration with orchestration tools

## Usage

1. Install dependencies (`pip install -r requirements.txt` or use poetry).
2. Set the `CLAUDE_API_KEY` environment variable for LLM access.
3. Run the agent pipeline in your own script or via CLI/REST (coming soon).

## Structure

- `agent/` — All agent logic (pipeline, LLM, Kaggle, notebook)
- `runs/` — Run artifacts (created at runtime)
- `tests/` — Unit tests (expand as needed)

## Development

- Contributions welcome! Extend for new LLMs, agent strategies, or integrations.
