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

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

st.markdown("### ⚡ Quick Actions")

col1, col2 = st.columns(2)

with col1:
    explain_arch = st.button("Explain Repository Architecture")

with col2:
    list_modules = st.button("List Main Modules")

st.markdown("### 💡 Example Questions")

examples = [
    "How does request handling work?",
    "How does routing work?",
    "Where is authentication implemented?",
    "Explain the architecture of this repository"
]

selected_example = st.selectbox(
    "Choose an example question (optional)",
    [""] + examples
)

# Chat input
user_input = st.chat_input("Ask your own question")

question = None

# Priority order for question selection
if user_input:
    question = user_input
elif selected_example:
    question = selected_example
elif explain_arch:
    question = "Explain the architecture of this repository and main components"
elif list_modules:
    question = "List the main modules of this repository and what they do"

# If user asked something
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

    answer = result.get("answer", "No response received.")

    st.chat_message("assistant").write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    # Show sources
    if "sources" in result:

        st.markdown("### 📂 Sources")

        for src in result["sources"]:
            st.code(src)