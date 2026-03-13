import faiss
import pickle
import numpy as np


def load_vector_store():

    index = faiss.read_index("data/vector_db/index.faiss")

    with open("data/vector_db/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    with open("data/vector_db/documents.pkl", "rb") as f:
        documents = pickle.load(f)

    return index, vectorizer, documents


def search_code(query, vector_db_path, top_k=5):

    import faiss
    import pickle
    import numpy as np

    index = faiss.read_index(f"{vector_db_path}/index.faiss")

    with open(f"{vector_db_path}/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    with open(f"{vector_db_path}/documents.pkl", "rb") as f:
        documents = pickle.load(f)

    query_vector = vectorizer.transform([query]).toarray()

    distances, indices = index.search(
        np.array(query_vector).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(documents[idx])

    return results

    index, vectorizer, documents = load_vector_store()

    query_vector = vectorizer.transform([query]).toarray()

    distances, indices = index.search(
        np.array(query_vector).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:

        results.append(documents[idx])

    return results