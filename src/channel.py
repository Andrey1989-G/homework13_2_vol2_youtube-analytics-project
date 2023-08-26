from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key = 'AIzaSyAxQ9B1lWmxKX9NdnhuAgj426ABx60C4Y8'


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        res = self.channel
        # res = self.printj()
        print(res['items'][0]['snippet']['description'])
