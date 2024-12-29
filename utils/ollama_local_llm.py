from ollama import chat
from ollama import ChatResponse

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


stream = chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)