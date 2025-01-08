from ollama import chat
from ollama import ChatResponse
import os


def ollama_llm_talk(transcript):


  print("Waiting for LLM Response...")
  stream = chat(
      model='llama3.2',
      messages=[{'role': 'user', 'content': f"""
                Given the following transcript of a video or lecture, identify and infer the most practical and actionable steps the viewer can implement immediately. Focus on:

                Specific actions: Clearly state what the viewer should do, breaking down complex tasks into manageable steps.
                Instructions: Explain how to carry out each action effectively, referencing relevant tools or methods when applicable.
                Effectiveness: Highlight why each step is impactful or beneficial.
                Present the response as a concise, numbered list in a step-by-step format. Use plain language and avoid unnecessary details, repetition, or generalizations.

                Transcript: {transcript}
                """}],
      stream=True,
      )

  llm_response = ""
  for chunk in stream:
    llm_response += chunk['message']['content']
    print(chunk['message']['content'], end='', flush=True)

  #save llm response to a .txt file 
  project_root = os.path.dirname(os.path.abspath(__file__))
  text_folder = os.path.join(project_root, "../text_files")
  os.makedirs(text_folder, exist_ok = True)

  file_path = os.path.join(text_folder,"llm_response.txt")
  with open(file_path, "w", encoding="utf-8") as file:
    file.write(llm_response)