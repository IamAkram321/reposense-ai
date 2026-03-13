from app.retrieval.retriever import search_code
from app.llm.generator import generate_answer

query = "how does react handle hooks"

results = search_code(query)

answer = generate_answer(query, results)

print(answer)