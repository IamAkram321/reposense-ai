import os
import git

BASE_REPO_PATH = "data/repos"

def clone_repository(repo_url: str):

    os.makedirs(BASE_REPO_PATH, exist_ok=True)

    repo_name = repo_url.split("/")[-1]
    repo_path = os.path.join(BASE_REPO_PATH, repo_name)

    if os.path.exists(repo_path):
        return repo_path

    git.Repo.clone_from(repo_url, repo_path)

    return repo_path