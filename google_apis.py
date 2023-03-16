import os
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = 'client_secret.json'


def create_youtube_playlist():
    t0 = time.time()

    creds = authenticate()
    youtube = build('youtube', 'v3', credentials=creds)

    prefix = 'Cartoon Playlist'

    for i in range(1, 1001):
        title = f'{prefix} {i}'

        request = youtube.playlists().insert(
            part='snippet, status',
            body={
                'snippet': {
                    'title': title,
                    'description': 'This is a test playlist.'
                },
                'status': {
                    'privacyStatus': 'private'
                }
            }
        )
        response = request.execute()

        print(f'Created playlist with title "{response["snippet"]["title"]}" and ID "{response["id"]}".')

    t1 = time.time()
    print('It took', int(t1 - t0), 'seconds to create 1000 playlists')


def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/youtube'])

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', ['https://www.googleapis.com/auth/youtube'])
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds
