import streamlit as st
import requests

st.title("📚 AI-Powered Assignment System")

# Upload Assignments
st.header("Upload Assignment")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])
if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    res = requests.post("http://backend:8000/upload-assignment/", files=files)
    st.success(res.json()["message"])

# View Assignments
st.header("View Assignments")
assignments = requests.get("http://backend:8000/assignments/").json()
for a in assignments:
    st.write(f"📄 {a[1]}")

# AI Chatbot
st.header("Chat with AI")
query = st.text_input("Ask AI about assignments")
if st.button("Ask"):
    response = requests.post("http://backend:8000/chat/", json={"question": query}).json()
    st.write("🤖 AI:", response["response"])
