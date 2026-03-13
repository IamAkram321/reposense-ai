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
    "Where is request handling implemented?",
    "Explain the architecture of this repo",
    "How are routes registered?"
]

selected_example = st.selectbox(
    "Choose an example question (optional)",
    [""] + examples
)

custom_question = st.text_input(
    "Or type your own question"
)

question = custom_question if custom_question else selected_example


if st.button("Ask RepoSense"):

    if repo_url and question:

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

    else:
        st.warning("Please enter a question.")