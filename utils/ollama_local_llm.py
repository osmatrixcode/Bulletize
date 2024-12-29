from ollama import chat
from ollama import ChatResponse
import os

# try:
#     response: ChatResponse = chat(model='llama3.2', messages=[
#         {
#             'role': 'user',
#             'content': 'Why is the sky blue?',
#         },
#     ])
#     print(response['message']['content'])
#     print(response.message.content)
# except Exception as e:
#     print(f"Error: {e}")

filename = "yt_transcript.txt"
file_path = os.path.join("..","transcripts",filename)

with open(file_path, "r") as file:
  content = file.read()




stream = chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': f'Summarise this text from top to bottom, into one paragraph: {content}'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)