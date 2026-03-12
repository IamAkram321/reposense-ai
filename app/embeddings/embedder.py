def chunk_code(content, chunk_size=500, overlap=50):

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