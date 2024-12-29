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


              # You are an advanced summarisation and actionable insights assistant. Your job is to take in a transcript and generate the following outputs: 
              # 1. A **concise summary** of the podcast in no more than 5 bullet points, covering only the most critical and relevant points.
              # 2. **Three actionable steps** based on the content of the podcast, designed to provide practical and implementable advice for the user.

              #  The summary should:
              # - Use simple and clear language.
              # - Be optimized for someone with no prior context of the video.
              # - Focus on insights, advice, or takeaways directly useful to the read
               
              # Here is the transcript: 


stream = chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': f"""
You are an expert assistant specializing in extracting actionable steps and instructions from video transcripts. Your task is to process a transcript and provide the following outputs in **bullet-point format**, with a focus on **tasks to be done** based on the video content, without mentioning the creator or their actions.  

1. **Actionable Tasks (Steps to Implement):**  
   List clear, concise, and actionable tasks that the viewer can complete, based on the tutorial content. Each task should be specific and directly tell the user what to do without referencing the creator.  

2. **Additional Tips (Optional):**  
   List any tips, features, or tools that can help optimize the tasks.  
Here is the transcript to process:  

              {content}
              """}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)