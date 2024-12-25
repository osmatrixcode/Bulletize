from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os



open_more_script = "const showMoreButton = document.querySelector('tp-yt-paper-button#expand'); if (showMoreButton) {showMoreButton.click();} else {console.log('Show more button not found.');}"
open_transcript_box_script = "document.querySelector('button[aria-label=\\'Show transcript\\']').click();"
get_transcript_script="const transcript = [...document.querySelectorAll('.segment-text')].map(e => e.textContent).join(' '); console.log(transcript); return transcript"


def ytTranscript(url):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)

    time.sleep(5)
    driver.execute_script(open_more_script)
    print("opened the 'more' section")
    
    time.sleep(2)
    driver.execute_script(open_transcript_box_script)
    print("opened the 'transcript' box")
    
    time.sleep(20)
    transcript = driver.execute_script(get_transcript_script)
    print("outputted the actual transcript")
    print(transcript)
    
    # Save transcript to a .txt file
    project_root = os.path.dirname(os.path.abspath(__file__))
    transcripts_folder = os.path.join(project_root, "../transcripts")
    os.makedirs(transcripts_folder, exist_ok = True)

    file_path = os.path.join(transcripts_folder,"yt_transcript.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(transcript)


    # driver.quit()
