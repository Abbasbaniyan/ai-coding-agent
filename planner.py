from llm import ask_llm
import json

def create_plan(repo_tree, user_request):
    prompt = f"""
You are an expert software engineer.

Repository Structure:
{repo_tree}

User Request:
{user_request}

Analyze the repository carefully.

Identify EVERY file that may need to be modified.

Return ONLY valid JSON.

Format:

{{
    "files":[
        "...",
        "..."
    ],
    "plan":[
        "...",
        "...",
        "..."
    ]
}}

Rules:
- Return ALL relevant files.
- Think step by step.
- Do NOT return markdown.
- Do NOT explain anything.
"""

    response = ask_llm(prompt).strip()

    if response.startswith("```"):
        response = response.replace("```json","").replace("```","").strip()

    return json.loads(response)