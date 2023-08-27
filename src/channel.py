import os
from googleapiclient.discovery import build
import json
from dotenv import load_dotenv

class Channel:
    """Класс для ютуб-канала"""
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=Channel.api_key)
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        res = self.channel
        # res = self.printj()
        print(res['items'][0]['snippet']['description'])
