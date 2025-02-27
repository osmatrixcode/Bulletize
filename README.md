# 📜 Bulletize: YouTube Summary Tool

Transform YouTube videos into concise, actionable summaries with ease! Bulletize extracts transcripts, summarises key points, and delivers practical takeaways. This tool works best with self-improvement style videos!

---

## ✨ Features

- 🎥 **Input YouTube Link**: Provide a YouTube video URL, and the tool will fetch the transcript (if available).
- 📄 **Transcript Extraction**: Automatically retrieves and processes video transcripts.
- 🤖 **AI Summarisation**: Generates a concise, actionable summary from the transcript.
- 🌟 **Sleek Web Interface**: Built with TailwindCSS for an intuitive user experience.
- 🚀 **Local AI Support**: Powered by Ollama and llama3.2 for fast, local processing.
---

## 🚀 How It Works

1. **Submit a YouTube URL**: Enter a YouTube video URL.
2. **Transcript Extraction**: The tool then uses Selenium to retrieve the transcript.
3. **AI Summarisation**: The transcript is processed by a local LLM (llama3.2) using an optimised prompt to generate the summary.
4. **Result**: A concise summary and actionable steps are displayed on the web interface.

---

## 🔧 Installation

### Prerequisites

- Ollama: Ensure it's installed and running on your system.
- llama3.2: Download and configure the specified version.
- Python Virtual Environment: Use Conda or venv for environment isolation.


### Steps

1. Clone the Repository and ```cd``` to the repository location in your terminal.
2. Create a virtual environment (e.g., using Conda):
   ```
   conda create --name <name for your environment>
   ```
3. Activate the environment and install pip:
   ```
   conda activate <your_environment_name>  
   conda install pip
   ```
4. Use pip to install the dependencies listed in requirements.txt:
   ```
   pip install -r requirements.txt
   ```
5. ```cd``` to the "web" folder in this repository and run the flask server using the following command:
   ```
   flask run
   ```
6. Make sure you have Ollama running in your local system.
7. Open the Flask server's URL in your web browser to start using Bulletize.

