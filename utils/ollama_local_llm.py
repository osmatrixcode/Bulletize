from ollama import chat
from ollama import ChatResponse
import os


def ollama_llm_talk(transcript):

# filename = "yt_transcript.txt"
# file_path = os.path.join("..","transcripts",filename)

# with open(file_path, "r") as file:
#   content = file.read()
  print("Waiting for LLM Response...")
  stream = chat(
      model='llama3.2',
      messages=[{'role': 'user', 'content': f"""
                in this text, find the most important parts (why important) and actionable steps to take

                {transcript}
                """}],
      stream=True,
      )

  for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)