import anthropic
import os
from dotenv import load_dotenv

load_dotenv()


client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))  # reads ANTHROPIC_API_KEY from env


def chat(messages: list) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=512,
        system="You are a concise voice assistant. Keep responses under 3 sentences.",
        messages=messages
    )
    return response.content[0].text
