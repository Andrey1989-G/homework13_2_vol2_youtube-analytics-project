import os
from googleapiclient.discovery import build
import json
from dotenv import load_dotenv

class Video:
    """Класс для видео"""
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, video_id: str):
        self.video_id = video_id
        try:
            self.youtube = build('youtube', 'v3',
                                   developerKey=Video.api_key)
            self.youtube_video = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
            self.url = self.youtube_video['items'][0]['snippet']['thumbnails']['default']['url']
            self.title = self.youtube_video['items'][0]['snippet']['title']
            self.view_count = self.youtube_video['items'][0]['statistics']['viewCount']
            self.like_count = self.youtube_video['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.like_count = None
            self.view_count = None

    # def __str__(self):
    #     return f'{self.url}\n{self.view_count}\n{self.like_count}\n{self.name_video}'

    # def to_json(self, file_name):
    #     """Сохраняет в файл значения атрибутов экземпляра `Channel`"""
    #     with open('moscowpython.json', 'w') as file_name:
    #         json.dump(self.youtube_video, file_name)

class PLVideo(Video):
    """Класс для плейлистов"""
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id

