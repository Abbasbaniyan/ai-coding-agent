from pathlib import Path


def validate_code(file_path):
    path = Path(file_path)

    if not path.exists():
        return False, "File not found"

    content = path.read_text(encoding="utf-8")

    if len(content.strip()) == 0:
        return False, "Generated file is empty"

    if "```" in content:
        return False, "Markdown detected in generated code"

    return True, "Validation passed"