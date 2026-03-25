# Classifier AI Agent

A small Python project that demonstrates how to use generative AI models to classify and prioritize tasks. This repo includes two variants:

- **`task_agent-open.py`**: Uses OpenAI's `gpt-3.5-turbo` chat completion API.
- **`task_agent-gem.py`**: Uses Google Gemini (via `google.generativeai`) to perform the same task.

The core idea is simple: load a list of tasks from `tasks.txt`, send them to an LLM, and ask the model to categorize the tasks into **High**, **Medium**, and **Low** priority.

---

## Features

- Reads task list from a plain text file (`tasks.txt`).
- Sends the task list to an LLM with a fixed prompt asking for priority classification.
- Prints a formatted summary with priority categories.

---

## Prerequisites

- Python 3.10+ 
- An OpenAI API key (for `task_agent-open.py`) **OR** a Google Gemini API key (for `task_agent-gem.py`)

---

## Installation

1. Clone the repo (or download the files).
2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, you can install just what’s needed:
>
> ```bash
> pip install python-dotenv openai google-generativeai
> ```

---

## Configuration

Copy the example env file and set your API key:

```bash
cp .env-example .env
```

Then edit `.env` and set one or both keys depending on which script you want to run:

- `OPENAI_API_KEY` — for `task_agent-open.py`
- `GEMINI_API_KEY` — for `task_agent-gem.py`

---

## Usage

### Run the OpenAI variant

```bash
python task_agent-open.py
```

### Run the Gemini variant

```bash
python task_agent-gem.py
```

Each script reads `tasks.txt`, sends a prompt to the model, and prints a prioritized list.

---

## Customizing the Task List

Edit `tasks.txt` with one task per line. Example:

```
Update the homepage UI
Fix login bug
Schedule team standup
```

---

## How It Works (Quick Overview)

Each script:

1. Loads `tasks.txt` into a string.
2. Builds a prompt asking the model to categorize tasks into High/Medium/Low priority.
3. Sends the prompt to the selected API.
4. Prints the model’s response.
