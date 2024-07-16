from promptflow import tool
from openai import OpenAI

@tool
def ollama(tweet_request: str, model: str) -> str:
    ollama_client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

    response = ollama_client.chat.completions.create(
        model = model,
        temperature = 1.0,
        messages = [
            {
                "role": "system",
                "content": tweet_request
            }
        ]
    )
    
    return response.choices[0].message.content
