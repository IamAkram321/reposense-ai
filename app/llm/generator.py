def build_prompt(query, retrieved_chunks):

    context = ""

    for chunk in retrieved_chunks:

        context += f"\nFile: {chunk['path']}\n"
        context += chunk["content"][:800]
        context += "\n\n"

    prompt = f"""
You are a senior software engineer helping understand a codebase.

Answer the following question based on the provided code snippets.

Question:
{query}

Code Snippets:
{context}

Explain clearly where the logic exists and how it works.
"""

    return prompt

def generate_answer(query, retrieved_chunks):

    prompt = build_prompt(query, retrieved_chunks)

    # For now we will just return the prompt
    # Later we will connect to an LLM

    return prompt