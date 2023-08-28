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
        # self.__channel_id = channel_id
        self.__channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=Channel.api_key)
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    # def __setattr__(self, key, value):
    #     if key == 'channel_id' and not value:
    #         raise AttributeError("property 'channel_id' of 'Channel' object has no setter")
    #     self.__dict__['channel_id'] = value

    @property
    def channel_id(self):
        return self.__channel_id
    @channel_id.setter
    def channel_id(self, channel_id):
        self.__channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        res = self.channel
        print(res['items'][0]['snippet']['description'])

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls

    def to_json(self, file_name):
        """Сохраняет в файл значения атрибутов экземпляра `Channel`"""
        with open('moscowpython.json', 'w') as file_name:
            json.dump(self.channel, file_name)
