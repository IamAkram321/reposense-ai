import streamlit as st
import requests

st.title("RepoSense AI")

st.write("Ask questions about any GitHub repository")

repo_url = st.text_input("GitHub Repository URL")

question = st.text_input("Ask a question about the code")

if st.button("Ask RepoSense"):

    if repo_url and question:

        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={
                "repo_url": repo_url,
                "question": question
            }
        )

        result = response.json()

        st.subheader("Answer")

        st.write(result["answer"])

    else:

        st.warning("Please provide both repo URL and question")