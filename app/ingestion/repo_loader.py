import os
import git

BASE_REPO_PATH = "data/repos"

SUPPORTED_EXTENSIONS = [
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".cpp",
    ".java",
    ".go",
    ".rs",
]

IGNORED_DIRS = [
    "node_modules",
    ".git",
    "__pycache__",
    "dist",
    "build",
    ".next",
]

IGNORED_FILES_PREFIX = [
    ".",
    "babel",
    "webpack",
]

# Maximum allowed file size (200 KB)
MAX_FILE_SIZE = 200 * 1024


def clone_repository(repo_url: str):

    os.makedirs(BASE_REPO_PATH, exist_ok=True)

    repo_name = repo_url.rstrip("/").split("/")[-1]

    repo_path = os.path.join(BASE_REPO_PATH, repo_name)

    if os.path.exists(repo_path):
        return repo_path

    print(f"Cloning repository: {repo_url}")

    git.Repo.clone_from(repo_url, repo_path)

    return repo_path


def load_code_files(repo_path):

    code_files = []

    for root, dirs, files in os.walk(repo_path):

        # Prevent scanning useless directories
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]

        for file in files:

            # Ignore hidden/config files
            if any(file.startswith(prefix) for prefix in IGNORED_FILES_PREFIX):
                continue

            if not any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                continue

            file_path = os.path.join(root, file)

            # Skip large files
            if os.path.getsize(file_path) > MAX_FILE_SIZE:
                continue

            try:

                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                code_files.append({
                    "path": file_path.replace("\\", "/"),
                    "content": content
                })

            except Exception:
                continue

    return code_files