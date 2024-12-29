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
                Given the following transcript of a video or lecture, extract the most practical and actionable steps or key takeaways. 
                The output should be concise and focused on specific actions, strategies, or advice that can be immediately implemented.
                Avoid generalizations or irrelevant details.
                Present the steps in a clear, actionable format

                here is the transcript:
                {transcript}
                """}],
      stream=True,
      )

  for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)