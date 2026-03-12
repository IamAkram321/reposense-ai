import os
import git

BASE_REPO_PATH = "data/repos"

SUPPORTED_EXTENSIONS = [".py", ".js", ".ts", ".tsx", ".cpp", ".java"]


def clone_repository(repo_url: str):

    os.makedirs(BASE_REPO_PATH, exist_ok=True)

    repo_name = repo_url.split("/")[-1]
    repo_path = os.path.join(BASE_REPO_PATH, repo_name)

    if os.path.exists(repo_path):
        return repo_path

    git.Repo.clone_from(repo_url, repo_path)

    return repo_path


def load_code_files(repo_path):

    code_files = []

    for root, dirs, files in os.walk(repo_path):

        # prevent scanning useless directories
        dirs[:] = [d for d in dirs if d not in ["node_modules", ".git", "__pycache__"]]

        for file in files:

            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):

                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    code_files.append({
                        "path": file_path,
                        "content": content
                    })

                except Exception:
                    continue

    return code_files