import streamlit as st
import requests

API_URL = "https://reposense-ai.onrender.com/ask"

st.title("RepoSense AI")
st.write("Ask questions about any GitHub repository")

repo_url = st.text_input(
    "GitHub Repository URL",
    "https://github.com/pallets/flask"
)

st.markdown("### Example Questions")

examples = [
    "How does Flask routing work?",
    "How are requests handled in this repo?",
    "Where is the authentication logic?",
    "Explain the architecture of this project."
]

question = st.selectbox("Choose a question", examples)

if st.button("Ask RepoSense"):

    with st.spinner("Analyzing repository..."):

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