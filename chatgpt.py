
import helpers

def count_tokens(text,selected_model):
    encoding = tiktoken.encoding_for_model(selected_model)
    num_tokens = encoding.encode(text)
    return len(num_tokens)

def generate_text_with_openai(user_prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # you can replace this with your preferred model
        messages=[{"role": "user", "content": user_prompt}],
    )
    return completion.choices[0].message.content



prompt ="Give me 5 catchy youtube titles about [drawing koala]"

#response = generate_text_with_openai(prompt)

#print(response)

num_tokens = count_tokens(prompt,"gpt-3.5-turbo")
print(f"token count = {num_tokens}")