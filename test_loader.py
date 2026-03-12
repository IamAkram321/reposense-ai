from app.ingestion.repo_loader import load_code_files
from app.embeddings.embedder import prepare_documents

files = load_code_files("data/repos/react")
docs = prepare_documents(files)

print(len(docs))