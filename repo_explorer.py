import os

IGNORE_DIRS = {
    ".git",
    "node_modules",
    "venv",
    "__pycache__",
    "dist",
    "build",
}


def build_repo_tree(root_path):
    tree = []

    for root, dirs, files in os.walk(root_path):

        # Ignore unnecessary folders
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        level = root.replace(root_path, "").count(os.sep)

        indent = "    " * level
        sub_indent = "    " * (level + 1)

        tree.append(f"{indent}{os.path.basename(root)}/")

        for file in files:
            if file.endswith(".bak"):
                continue

            tree.append(f"{sub_indent}{file}")

    return "\n".join(tree)