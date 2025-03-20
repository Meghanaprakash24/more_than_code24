import streamlit as st
import requests

st.title("🤖 AI Chatbot - Ask Questions")

st.write("This AI chatbot can answer assignment-related questions.")

# Input field for user query
query = st.text_input("Ask AI a question about assignments")

if st.button("Ask"):
    if query:
        response = requests.post("http://backend:8000/chat/", json={"question": query}).json()
        st.write("🤖 AI:", response["response"])
    else:
        st.warning("Please enter a question.")
