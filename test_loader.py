from app.ingestion.repo_loader import load_code_files

repo_path = "data/repos/react"

files = load_code_files(repo_path)

print("Total files loaded:", len(files))

print("\nExample file:\n")

print(files[0]["path"])
print(files[0]["content"][:200])