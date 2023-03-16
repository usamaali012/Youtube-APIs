import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Create a new Chrome driver instance

YOUTUBE_HOME_PAGE = 'https://www.youtube.com/'
GOOGLE_SIGN_IN_PAGE = 'https://accounts.google.com/signin'
# CHROME_PROFILE_PATH = r'C:\Users\CHI\AppData\Local\Google\Chrome\User Data\Profile 11'
CHROME_PROFILE_PATH = r'C:\Users\CHI\AppData\Local\Google\Chrome\User Data'


def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument(f'user-data-dir={CHROME_PROFILE_PATH}')
    chrome_options.add_argument("--profile-directory=Profile 11")
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=chrome_options)
    return driver


def create_youtube_playlist():
    driver = get_chrome_driver()
    driver.get(YOUTUBE_HOME_PAGE)
    wait = WebDriverWait(driver, 10)

    your_videos_css_selector = 'body > ytd-app:nth-child(4) > div:nth-child(7) > tp-yt-app-drawer:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ytd-guide-renderer:nth-child(1) > div:nth-child(1) > ytd-guide-section-renderer:nth-child(1) > div:nth-child(2) > ytd-guide-collapsible-section-entry-renderer:nth-child(4) > div:nth-child(2) > ytd-guide-entry-renderer:nth-child(2) > a:nth-child(1) > tp-yt-paper-item:nth-child(1) > yt-formatted-string:nth-child(3)'
    your_videos_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, your_videos_css_selector)))
    your_videos_element.click()

    create_path = "//div[contains(text(),'Create')]"
    create_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, create_path)))
    create_button_element.click()

    time.sleep(5)


create_youtube_playlist()
