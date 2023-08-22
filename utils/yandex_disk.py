import yadisk_async
from config import YA_TOKEN

class YandexDisk():
    def __init__(self):
        # Инициализация объекта для работы с Yandex Disk, передаем токен
        self.y = yadisk_async.YaDisk(token=YA_TOKEN)
        
    async def save_content(self, file_name, file_path):
        # Асинхронный метод для загрузки файла на Yandex Disk
        async with self.y as session:
            await session.upload(file_name, file_path)
            









