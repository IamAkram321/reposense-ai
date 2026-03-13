from fastapi import APIRouter
from pydantic import BaseModel

from app.ingestion.repo_loader import clone_repository, load_code_files
from app.embeddings.embedder import prepare_documents, build_vector_store, save_vector_store
from app.retrieval.retriever import search_code
from app.llm.generator import generate_answer

router = APIRouter()


class AskRequest(BaseModel):
    repo_url: str
    question: str


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

    # 1️⃣ Clone repo
    repo_path = clone_repository(repo_url)

    # 2️⃣ Load files
    code_files = load_code_files(repo_path)

    # 3️⃣ Prepare documents
    documents = prepare_documents(code_files)

    # 4️⃣ Build vector index
    index, vectorizer = build_vector_store(documents)

    # 5️⃣ Save vector database
    save_vector_store(index, vectorizer, documents)

    # 6️⃣ Retrieve relevant code
    results = search_code(question)

    # 7️⃣ Generate AI answer
    answer = generate_answer(question, results)

    return {
        "repository": repo_url,
        "question": question,
        "answer": answer
    }