from ollama import chat
from ollama import ChatResponse
import os


                # Given the following transcript of a video or lecture, extract the most practical and actionable steps or key takeaways. 
                # The output should be concise and focused on specific actions, strategies, or advice that can be immediately implemented, 
                # making sure it is practical exercises you can do right now. From these, can you generate some 'actionable' exercises, goals, tasks etc... 
                # Avoid generalizations or irrelevant details.
                # Present the steps in a clear, actionable format

                # here is the transcript:
                # {transcript}

def ollama_llm_talk(transcript):


  print("Waiting for LLM Response...")
  stream = chat(
      model='llama3.2',
      messages=[{'role': 'user', 'content': f"""
                Given the following transcript of a video or lecture, extract the most practical, 
                actionable steps for the viewer to implement immediately. Focus on the specific actions that should be taken, 
                how to do them, and why they are effective. Each action should include clear instructions, specific tools or resources,
                and tangible goals or tasks. Avoid generalizations and unnecessary details. Present the response in a clear,
                step-by-step format that emphasizes what needs to be done and how to execute it.

                Here is the transcript: {transcript}
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