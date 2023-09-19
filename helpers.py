

import openai
import tiktoken


# replace with your api key
openai.api_key = "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"



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

def estimate_input_cost(model_name, token_count):
    if model_name == "gpt-3.5-turbo-0613":
        cost_per_1000_tokens = 0.0015
    if model_name == "gpt-3.5-turbo-16k-0613":
        cost_per_1000_tokens = 0.003
    if model_name == "gpt-4-0613":
        cost_per_1000_tokens = 0.03
    if model_name == "gpt-4-32k-0613":
        cost_per_1000_tokens = 0.06
    estimated_cost = (token_count / 1000) * cost_per_1000_tokens
    return estimated_cost

def estimate_input_cost(model_name, token_count):
    # Define a dictionary mapping model names to costs
    model_costs = {
        "gpt-3.5-turbo-0613": 0.0015,
        "gpt-3.5-turbo-16k-0613": 0.003,
        "gpt-4-0613": 0.03,
        "gpt-4-32k-0613": 0.06,
    }
    
    # Get the cost per 1000 tokens for the given model
    # Raise an exception if the model is not recognized
    try:
        cost_per_1000_tokens = model_costs[model_name]
    except KeyError:
        raise ValueError(f"Unknown model: {model_name}")
    
    # Calculate the estimated cost
    estimated_cost = (token_count / 1000) * cost_per_1000_tokens
    
    return estimated_cost