import streamlit as st
import requests

st.title("📂 Upload & View Assignments")

# Upload Assignment
st.header("Upload Assignment")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])
if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    res = requests.post("http://backend:8000/upload-assignment/", files=files)
    st.success(res.json()["message"])

# View Uploaded Assignments
st.header("📜 Submitted Assignments")
assignments = requests.get("http://backend:8000/assignments/").json()
if assignments:
    for a in assignments:
        st.write(f"📄 **{a[1]}**")
else:
    st.write("No assignments uploaded yet.")

