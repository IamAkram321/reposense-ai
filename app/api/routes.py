from fastapi import APIRouter
from pydantic import BaseModel
import os

from app.ingestion.repo_loader import clone_repository, load_code_files
from app.embeddings.embedder import prepare_documents, build_vector_store, save_vector_store
from app.retrieval.retriever import search_code
from app.llm.generator import generate_answer

router = APIRouter()


class AskRequest(BaseModel):
    repo_url: str
    question: str


def get_repo_name(repo_url: str):
    return repo_url.rstrip("/").split("/")[-1]


@router.post("/ingest")
def ingest_repo(repo_url: str):

    repo_path = clone_repository(repo_url)

    return {
        "status": "success",
        "repo_path": repo_path
    }


@router.post("/ask")
def ask_question(data: AskRequest):

    repo_url = data.repo_url
    question = data.question

    repo_name = get_repo_name(repo_url)

    # repo specific vector db folder
    vector_db_path = f"data/vector_db/{repo_name}"

    # clone repo
    repo_path = clone_repository(repo_url)

    # build index only if it does not exist
    if not os.path.exists(f"{vector_db_path}/index.faiss"):

        print("Building vector database for repo:", repo_name)

        code_files = load_code_files(repo_path)

        documents = prepare_documents(code_files)

        index, vectorizer = build_vector_store(documents)

        save_vector_store(index, vectorizer, documents, vector_db_path)

    else:
        print("Using cached vector database for repo:", repo_name)

    # retrieve relevant code chunks
    results = search_code(question, vector_db_path)

    # generate answer using LLM
    answer = generate_answer(question, results)

    # extract source file paths
    sources = list({r["path"] for r in results})

    return {
        "repository": repo_url,
        "question": question,
        "answer": answer,
        "sources": sources
    }