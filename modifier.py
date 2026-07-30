from pathlib import Path
import shutil
from validator import validate_code
from llm import ask_llm


def modify_file(file_path, user_request):
    path = Path(file_path)

    if not path.exists():
        print(f"❌ File not found: {file_path}")
        return

    # Create backup
    backup_path = path.with_suffix(path.suffix + ".bak")
    shutil.copy(path, backup_path)

    print(f"📦 Backup created: {backup_path.name}")

    # Read original code
    original_code = path.read_text(encoding="utf-8")

    prompt = f"""
You are an expert Node.js developer.

User Request:
{user_request}

Existing Code:
{original_code}

Update the code according to the request.

Return ONLY the complete updated code.
Do not use markdown.
Do not include explanations.
"""

    updated_code = ask_llm(prompt).strip()

    # Remove markdown if Gemini returns ```javascript
    if updated_code.startswith("```"):
        updated_code = (
            updated_code.replace("```javascript", "")
                        .replace("```js", "")
                        .replace("```", "")
                        .strip()
        )

    # Safety check
    if not updated_code:
        print(f"❌ Empty response for {file_path}")
        return

    path.write_text(updated_code, encoding="utf-8")
    valid, message = validate_code(file_path)
    if valid:
        print(f"✅ Updated: {file_path}")
    else:
        print(f"❌ Validation failed: {message}")