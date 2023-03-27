import os
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


CLIENT_SECRETS_FILE = 'client_secret.json'


def create_youtube_playlist(secret_key):
    creds = authenticate()
    youtube = build('youtube', 'v3', credentials=creds, developerKey=secret_key)

    prefix = 'Original Cartoon Playlist Part-I'

    title = f'{prefix}'

    playlist_request = youtube.playlists().insert(
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
    playlist_response = playlist_request.execute()

    playlist_id = playlist_response["id"]
    print('playlist_id', playlist_id)

    with open("links.txt", "r") as file:
        links = file.readlines()

    for index, link in enumerate(links):
        video_id = link.split('=')[-1].strip()

        try:
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "kind": "youtube#playlistItem",
                    "snippet": {
                        "playlistId": playlist_id,
                        "position": index,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video_id
                        }
                    }
                }
            )
            request.execute()
            print(f'{video_id} video added to playlist {playlist_id}.')
        except HttpError as error:
            print(f'An error occurred: {error}')


def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', [
            'https://www.googleapis.com/auth/youtube',
            'https://www.googleapis.com/auth/youtube.force-ssl',
            'https://www.googleapis.com/auth/youtube.upload'
        ])

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', [
                'https://www.googleapis.com/auth/youtube',
                'https://www.googleapis.com/auth/youtube.force-ssl',
                'https://www.googleapis.com/auth/youtube.upload'
            ])
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def create_multiple_youtube_playlists():
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


def add_youtube_video(secret_key):
    creds = authenticate()
    youtube = build('youtube', 'v3', credentials=creds, developerKey=secret_key)

    title = 'Tech Video'
    description = 'This is a tech test video'
    tags = ['test', 'video', 'tech']
    privacy = 'public'

    # Define the video file path
    video_file_path = 'youtube_video.MOV'
    print('Uploading Video...')

    # Upload the video
    try:
        request = youtube.videos().insert(
            part='snippet,status',
            body={
                'snippet': {
                    'title': title,
                    'description': description,
                    'tags': tags
                },
                'status': {
                    'privacyStatus': privacy
                }
            },
            media_body=MediaFileUpload(video_file_path)
        )
        response = request.execute()

        print(f'Successfully uploaded video {response["id"]}')

    except HttpError as error:
        print(f'An error occurred: {error}')
