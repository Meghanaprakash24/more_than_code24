import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_questions(content):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Generate 5 questions from the given text."},
                  {"role": "user", "content": content}]
    )
    return response['choices'][0]['message']['content']
