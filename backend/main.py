from fastapi import FastAPI, UploadFile, File
from database import setup_db, store_assignment, get_assignments
from ai_utils import generate_questions
from chatbots import ask_ai
from auto_grading import grade_assignment

app = FastAPI()

# Initialize Database
setup_db()

@app.post("/upload-assignment/")
async def upload_assignment(file: UploadFile = File(...)):
    content = await file.read()
    store_assignment(file.filename, content)
    return {"message": "Assignment uploaded successfully"}

@app.get("/assignments/")
def list_assignments():
    return get_assignments()

@app.post("/generate-questions/")
def generate_assignment(content: str):
    questions = generate_questions(content)
    return {"questions": questions}

@app.post("/chat/")
def chat_with_ai(question: str):
    response = ask_ai(question)
    return {"response": response}

@app.post("/grade/")
def grade_submission(answer: str, correct_answer: str):
    return {"grade": grade_assignment(answer, correct_answer)}
