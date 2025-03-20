def grade_assignment(answer, correct_answer):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Compare the student's answer with the correct answer and grade it."},
                  {"role": "user", "content": f"Student Answer: {answer} \nCorrect Answer: {correct_answer}"}]
    )
    return response['choices'][0]['message']['content']
