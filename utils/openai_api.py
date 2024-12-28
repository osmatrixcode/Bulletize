from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
     api_key=os.environ.get("OPENAI_API_KEY")
)

print(os.environ.get("OPENAI_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo-1106",
)

print(chat_completion)