# AI Coding Agent

## Overview

AI Coding Agent is a Python-based tool that automates repository analysis and source code modification using Google's Gemini API.

The agent accepts a natural language request, explores the target repository, identifies the relevant files, generates an execution plan, modifies the code, validates the generated output, and produces a summary of all changes.

---

## Features

- Repository exploration
- Automatic relevant file detection
- AI-powered execution planning
- AI-powered code modification
- Automatic backup creation
- Code validation
- Summary generation
- Logging

---

## Architecture

```
                 User Request
                       │
                       ▼
              Repository Explorer
                       │
                       ▼
               Gemini Planner
                       │
                       ▼
          Relevant File Identification
                       │
                       ▼
              Backup Original Files
                       │
                       ▼
             AI Code Modification
                       │
                       ▼
                Code Validation
                       │
                       ▼
             Summary Generation
                       │
                       ▼
                    Logging
```

---

## Agent Workflow

1. Accept a natural language request.
2. Explore the repository structure.
3. Send the repository tree and request to Gemini.
4. Generate an execution plan.
5. Identify relevant source files.
6. Create backup copies of files.
7. Modify files using Gemini.
8. Validate generated code.
9. Generate a summary report.

---

## Repository Exploration

The repository is explored recursively using Python's `os.walk()`.

Ignored directories:

- .git
- node_modules
- venv
- __pycache__
- build
- dist

The generated repository tree is passed to the planner so the LLM can understand the project structure before selecting files.

---

## Assumptions

- The repository is already cloned locally.
- Gemini returns valid source code.
- The requested feature can be implemented by modifying existing files.

---

## Trade-offs

Current implementation focuses on simplicity.

Future improvements:

- AST-based repository analysis
- Automatic syntax checking
- Automatic rollback on validation failure
- Unit test execution
- Multi-language support

---

## Installation

```bash
git clone https://github.com/Abbasbaniyan/ai-coding-agent.git

cd ai-coding-agent

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

## Usage

```bash
python agent.py
```

Example Request

```
Improve the application so users can better organise and search their notes.
```

---

## Technologies

- Python 3.11
- Google Gemini API
- python-dotenv
- GitPython
- pathlib

---

## Project Structure

```
ai-coding-agent/

│── agent.py
│── planner.py
│── modifier.py
│── repo_explorer.py
│── validator.py
│── summary.py
│── logger.py
│── llm.py
│── config.py
│── requirements.txt
│── output/
│── logs/
│── repos/
│── README.md
```

---

## Future Improvements

- Support multiple programming languages
- Automatic testing after modifications
- Smarter repository indexing
- Interactive approval before writing changes
- Better semantic code search
