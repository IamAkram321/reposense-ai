from fastapi import APIRouter
from app.ingestion.repo_loader import clone_repository

router = APIRouter()

@router.post("/ingest")
def ingest_repo(repo_url: str):

    repo_path = clone_repository(repo_url)

    return {
        "status": "success",
        "repo_path": repo_path
    }