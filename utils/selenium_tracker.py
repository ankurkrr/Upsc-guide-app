from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.stopwatch import Stopwatch
import time

def track_youtube_video(video_url, duration=60):
    driver = webdriver.Chrome()  # Ensure chromedriver is installed
    driver.get(video_url)

    video_state_script = """
        var video = document.querySelector('video');
        return video.paused ? 'paused' : 'playing';
    """

    stopwatch = Stopwatch()
    start_time = time.time()

    while time.time() - start_time < duration:
        video_state = driver.execute_script(video_state_script)
        if video_state == "playing":
            stopwatch.start()
        elif video_state == "paused":
            stopwatch.stop()
        time.sleep(1)

    driver.quit()
    return stopwatch.get_time()
