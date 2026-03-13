import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def build_prompt(query, retrieved_chunks):

    context = ""

    for chunk in retrieved_chunks:

        context += f"\nFile: {chunk['path']}\n"
        context += chunk["content"][:800]
        context += "\n\n"

    prompt = f"""
You are a senior software engineer helping understand a codebase.

Answer the question using the provided code snippets.

Question:
{query}

Code Snippets:
{context}

Explain clearly where the logic exists and how it works.
"""

    return prompt


def generate_answer(query, retrieved_chunks):

    prompt = build_prompt(query, retrieved_chunks)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content