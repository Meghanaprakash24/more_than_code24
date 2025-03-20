import streamlit as st
import requests

st.title("📝 AI-Powered Quiz")

# Enter Study Material to Generate Quiz
st.header("Generate AI Quiz")
study_material = st.text_area("Paste your study material or notes")

if st.button("Generate Questions"):
    if study_material:
        response = requests.post("http://backend:8000/generate-questions/", json={"content": study_material}).json()
        st.write("📚 **AI-Generated Questions:**")
        for i, q in enumerate(response["questions"].split("\n"), 1):
            st.write(f"{i}. {q}")
    else:
        st.warning("Please enter some study material.")
