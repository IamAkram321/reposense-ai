import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
import numpy as np


def chunk_code(content, chunk_size=800, overlap=100):

    chunks = []

    start = 0

    while start < len(content):

        end = start + chunk_size
        chunk = content[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def prepare_documents(code_files):

    documents = []

    for file in code_files:

        content = file["content"]

        if not content.strip():
            continue

        chunks = chunk_code(content)

        for chunk in chunks:

            documents.append({
                "content": chunk,
                "path": file["path"]
            })

    return documents


def build_vector_store(documents):

    texts = [doc["content"] for doc in documents]

    vectorizer = TfidfVectorizer(max_features=5000)

    X = vectorizer.fit_transform(texts).toarray()

    dimension = X.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(X).astype("float32"))

    return index, vectorizer


def save_vector_store(index, vectorizer, documents, vector_db_path):

    import os
    import pickle
    import faiss

    os.makedirs(vector_db_path, exist_ok=True)

    faiss.write_index(index, f"{vector_db_path}/index.faiss")

    with open(f"{vector_db_path}/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    with open(f"{vector_db_path}/documents.pkl", "wb") as f:
        pickle.dump(documents, f)

    os.makedirs("data/vector_db", exist_ok=True)

    faiss.write_index(index, "data/vector_db/index.faiss")

    with open("data/vector_db/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    with open("data/vector_db/documents.pkl", "wb") as f:
        pickle.dump(documents, f)

    os.makedirs("data/vector_db", exist_ok=True)

    faiss.write_index(index, "data/vector_db/index.faiss")

    with open("data/vector_db/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)