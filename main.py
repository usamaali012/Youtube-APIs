import os
from dotenv import load_dotenv
from google_apis import create_youtube_playlist

# from selenium_tool import create_youtube_playlist, add_video_to_playlist

if __name__ == '__main__':
    load_dotenv()
    secret_key = os.getenv('YOUTUBE_API_KEY')
    create_youtube_playlist(secret_key)
    # add_video_to_playlist()

