import os
from dotenv import load_dotenv
from youtube_apis import create_youtube_playlist

if __name__ == '__main__':
    load_dotenv()
    secret_key = os.getenv('YOUTUBE_API_KEY')
    create_youtube_playlist()
