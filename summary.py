from pathlib import Path

def generate_summary(user_request, plan):
    output = Path("output/summary.md")

    text = f"""# AI Coding Agent Summary

## User Request

{user_request}

## Files Modified

"""

    for file in plan["files"]:
        text += f"- {file}\n"

    text += "\n## Execution Plan\n\n"

    for i, step in enumerate(plan["plan"], start=1):
        text += f"{i}. {step}\n"

    text += """

## Status

✅ Repository explored successfully

✅ Relevant files identified

✅ Backup files created

✅ AI generated code modifications

✅ Changes written to repository

"""
    output.write_text(text, encoding="utf-8")

    print("📝 Summary generated: output/summary.md")