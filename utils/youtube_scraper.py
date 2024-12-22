from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

get_transcript_script="const transcript = [...document.querySelectorAll('.segment-text')].map(e => e.textContent).join(' '); console.log(transcript);"
open_more_script = "const showMoreButton = document.querySelector('tp-yt-paper-button#expand'); if (showMoreButton) {showMoreButton.click();} else {console.log('Show more button not found.');}"

def ytTranscript(url):
    options = Options()
    options.add_argument("__headless")
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    time.sleep(5)
    driver.execute_script(open_more_script)
    # driver.execute_script("const transcript = [...document.querySelectorAll('.segment-text')].map(e => e.textContent).join(' '); console.log(transcript);")
    print("ytTranscript function running!")
    # driver.quit()
