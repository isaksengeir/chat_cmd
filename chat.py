#!/usr/bin/env python3

from openai import OpenAI

# Sett opp API-nøkkelen din fra https://beta.openai.com/account/api-keys
api_key = ''
client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(model=model,
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message["content"]

if __name__ == "__main__":
    while True:
        user_input = input("Du: ")
        if user_input.lower() == 'exit':
            break
        response = chat_with_gpt(user_input)
        print("GPT: " + response)






