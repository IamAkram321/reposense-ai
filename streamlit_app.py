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

if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

question = st.chat_input("Ask a question about the repository")

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

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

    answer = result["answer"]

    st.chat_message("assistant").write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    if "sources" in result:

        st.markdown("### 📂 Sources")

        for src in result["sources"]:
            st.code(src)