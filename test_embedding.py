from app.ingestion.repo_loader import load_code_files
from app.embeddings.embedder import prepare_documents, build_vector_store, save_vector_store

repo_path = "data/repos/react"

files = load_code_files(repo_path)

documents = prepare_documents(files)

print("Total documents:", len(documents))

index, vectorizer = build_vector_store(documents)

save_vector_store(index, vectorizer, documents)

print("Vector database created successfully!")