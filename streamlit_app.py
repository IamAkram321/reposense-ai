import streamlit as st
import requests

API_URL = "https://reposense-ai.onrender.com/ask"

st.set_page_config(page_title="RepoSense AI", page_icon="🔍")

st.title("🔍 RepoSense AI")
st.caption("Ask questions about any GitHub repository")

repo_url = st.text_input(
    "GitHub Repository URL",
    "https://github.com/pallets/flask"
)

examples = [
    "How does Flask routing work?",
    "Where are routes defined?",
    "Explain the architecture of this repo",
    "How are requests handled?"
]

selected_example = st.selectbox(
    "Example questions (optional)",
    [""] + examples
)

user_input = st.chat_input("Ask your question")

question = user_input if user_input else selected_example

if question:

    st.chat_message("user").write(question)

    with st.spinner("Analyzing repository..."):

        response = requests.post(
            API_URL,
            json={
                "repo_url": repo_url,
                "question": question
            }
        )

        result = response.json()

    st.chat_message("assistant").write(result["answer"])