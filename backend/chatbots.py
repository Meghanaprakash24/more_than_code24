def ask_ai(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Answer assignment-related questions."},
                  {"role": "user", "content": question}]
    )
    return response['choices'][0]['message']['content']
