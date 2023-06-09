import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


YOUTUBE_HOME_PAGE = 'https://www.youtube.com/'
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
    t0 = time.time()

    driver = get_chrome_driver()
    driver.get(YOUTUBE_HOME_PAGE)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    your_videos_css_selector = 'body > ytd-app:nth-child(4) > div:nth-child(7) > tp-yt-app-drawer:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ytd-guide-renderer:nth-child(1) > div:nth-child(1) > ytd-guide-section-renderer:nth-child(1) > div:nth-child(2) > ytd-guide-collapsible-section-entry-renderer:nth-child(4) > div:nth-child(2) > ytd-guide-entry-renderer:nth-child(2) > a:nth-child(1) > tp-yt-paper-item:nth-child(1) > yt-formatted-string:nth-child(3)'
    your_videos_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, your_videos_css_selector)))
    your_videos_element.click()

    new_tab = driver.window_handles[-1]
    driver.switch_to.window(new_tab)

    title_prefix = 'Testing2 Playlist'

    for i in range(1, 1001):
        create_path = r"create-icon"
        create_button_element = wait.until(EC.element_to_be_clickable((By.ID, create_path)))
        create_button_element.click()

        new_playlist_path = "body > ytcp-app:nth-child(2) > ytcp-entity-page:nth-child(9) > div:nth-child(2) > ytcp-header:nth-child(3) > header:nth-child(1) > div:nth-child(4) > ytcp-text-menu:nth-child(8) > tp-yt-paper-dialog:nth-child(1) > tp-yt-paper-listbox:nth-child(2) > tp-yt-paper-item:nth-child(5) > ytcp-ve:nth-child(1) > div:nth-child(6) > div:nth-child(1) > yt-formatted-string:nth-child(2)"
        new_playlist_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, new_playlist_path)))
        new_playlist_element.click()

        title_x_path = "//ytcp-social-suggestions-textbox[@id='title-textarea']//div[@id='textbox']"
        title_element = wait.until(EC.element_to_be_clickable((By.XPATH, title_x_path)))
        title_element.send_keys(f'{title_prefix} {i}')

        save_button_x_path = "ytcp-button[id='create-button'] div[class='label style-scope ytcp-button']"
        save_button_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, save_button_x_path)))
        save_button_element.click()

        if i == 1:
            time.sleep(10)
        else:
            time.sleep(3)

        print(f'Playlist {i} Created')

    t1 = time.time()
    print('It took', round((t1 - t0), 1), 'Seconds TO create 1000 Playlist')


def add_video_to_playlist():
    driver = get_chrome_driver()
    driver.get(YOUTUBE_HOME_PAGE)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    your_videos_css_selector = 'body > ytd-app:nth-child(4) > div:nth-child(7) > tp-yt-app-drawer:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ytd-guide-renderer:nth-child(1) > div:nth-child(1) > ytd-guide-section-renderer:nth-child(1) > div:nth-child(2) > ytd-guide-collapsible-section-entry-renderer:nth-child(4) > div:nth-child(2) > ytd-guide-entry-renderer:nth-child(2) > a:nth-child(1) > tp-yt-paper-item:nth-child(1) > yt-formatted-string:nth-child(3)'
    your_videos_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, your_videos_css_selector)))
    your_videos_element.click()

    new_tab = driver.window_handles[-1]
    driver.switch_to.window(new_tab)

    playlist_tab_x_path = "//span[normalize-space()='Playlists']"
    playlist_tab_element = wait.until(EC.element_to_be_clickable((By.XPATH, playlist_tab_x_path)))
    playlist_tab_element.click()

    playlist_x_path = "//body/ytcp-app/ytcp-entity-page[@id='entity-page']/div[@id='main-container']/div[@class='nav-and-main-content style-scope ytcp-entity-page']/main[@id='main']/div[@class='all-pages style-scope ytcp-app']/ytcp-animatable[@name='channel.videos']/ytcp-content-section[@id='video-list']/ytcp-playlist-section[@id='playlist-section']/ytcp-playlist-section-content[@class='style-scope ytcp-playlist-section']/div[@id='playlist-table-content']/ytcp-playlist-row[1]/div[1]/div[1]/div[1]/a[1]/ytcp-playlist-thumbnail[1]/div[1]"
    playlist_element = wait.until(EC.element_to_be_clickable((By.XPATH, playlist_x_path)))
    playlist_element.click()

    third_tab = driver.window_handles[-1]
    driver.switch_to.window(third_tab)

    time.sleep(5)
    # three_dots_button_x_path = "//yt-button-shape[@version='modern']//div[2]"
    three_dots_button_x_path = "yt-button-shape[version='modern'] div:nth-child(2)"
    three_dots_button_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, three_dots_button_x_path)))
    three_dots_button_element.click()

    add_videos_x_path = "//body[1]/ytd-app[1]/ytd-popup-container[1]/tp-yt-iron-dropdown[1]/div[1]/ytd-menu-popup-renderer[1]/tp-yt-paper-listbox[1]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item[1]"
    add_videos_element = wait.until(EC.element_to_be_clickable((By.XPATH, add_videos_x_path)))
    add_videos_element.click()

    link = 'https://www.youtube.com/watch?v=l3zyyvZz0RE'


# playlist_x_path = "//ytcp-playlist-row[1]//div[1]//div[1]//div[1]//a[1]//ytcp-playlist-thumbnail[1]//ytcp-img-with-fallback[1]//div[1]//img[1]"
# move to second page
# three_dots_button_x_path = "button[aria-label='Action menu'] div[class='yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response']"
# add_videos_x_path = "ytd-menu-service-item-renderer[class='style-scope ytd-menu-popup-renderer iron-selected'] tp-yt-paper-item[role='option']"
# search_button_selector = "body"