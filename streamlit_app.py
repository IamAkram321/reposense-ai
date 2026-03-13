import streamlit as st
import requests

API_URL = "https://reposense-ai.onrender.com/ask"

st.title("RepoSense AI")

st.write("Ask questions about any GitHub repository")

repo_url = st.text_input("GitHub Repository URL")

question = st.text_input("Ask a question about the code")

if st.button("Ask RepoSense"):

    if repo_url and question:

        response = requests.post(
            API_URL,
            json={
                "repo_url": repo_url,
                "question": question
            }
        )

        result = response.json()

        st.subheader("Answer")

        st.write(result["answer"])

    else:
        st.warning("Please provide repo URL and question")