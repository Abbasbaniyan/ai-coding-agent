from repo_explorer import build_repo_tree
from planner import create_plan
from modifier import modify_file
from summary import generate_summary
from config import REPO_PATH

repo_tree = build_repo_tree(REPO_PATH)

print("=" * 60)
print("Repository Structure")
print("=" * 60)
print(repo_tree)

request = input("\nWhat changes do you want to make?\n> ")

plan = create_plan(repo_tree, request)

print("\nRelevant Files:")
for file in plan["files"]:
    print("-", file)

print("\nExecution Plan:")
for step in plan["plan"]:
    print("-", step)

print("\nModifying Files...\n")

for file in plan["files"]:
    full_path = f"{REPO_PATH}/{file}"
    modify_file(full_path, request)

generate_summary(request, plan)