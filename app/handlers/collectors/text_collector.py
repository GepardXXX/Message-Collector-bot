import os
import datetime
from aiogram.types import ContentType, Message
from .media_collector import MediaCollector  # Импорт базового класса MediaCollector
from aiomisc.io import async_open


class TextCollector(MediaCollector):
    def __init__(self):
        super().__init__()
        self.file_name = self.get_formatted_date()  # Генерация имени файла на основе даты
        self.content_types = [ContentType.TEXT]  # Указание поддерживаемых типов контента
    

    async def collect_text_message(self, message: Message):
        message_text = message.text
        formatted_date = self.get_formatted_date()
        user_name = self.get_user_name(message)
        full_message = self.generate_full_message(formatted_date, user_name, message_text)

        file_name = f'{self.file_name}.txt'
        async with async_open(file_name, 'a', encoding='utf-8') as f:
            await f.write(full_message)  # Запись сообщения в файл
        await self.check_file(file_name)  # Проверка файла и загрузка на Яндекс.Диск при необходимости

    async def check_file(self, file_name):
        async with async_open(file_name, encoding='utf-8') as f:
            file = await f.read()

        if file.count('\t') >= 100:  # Если количество сообщений достигает 100
            new_date = self.get_formatted_date()
            new_file_name = f'{file_name}~{new_date}.txt'

            os.rename(file_name, new_file_name)  # Переименование файла с дополнительной датой
            await self.upload_to_yandex_disk(file_path=f'your/path{new_file_name}', file_name=new_file_name)  # Загрузка на Яндекс.Диск

    
    def get_user_name(self, message: Message):
        return super().get_user_name(message)  # Вызов метода родительского класса

    def get_formatted_date(self):
        date = datetime.datetime.now()
        return date.strftime("%Y-%m-%d %H-%M")  # Форматирование текущей даты

    def generate_full_message(self, formatted_date, user_name, message_text):
        return f'{formatted_date}\t{user_name} - {message_text}\n\n'  # Генерация полного сообщения

    async def upload_to_yandex_disk(self, file_name, file_path):
        await super().upload_to_yandex_disk(file_name, file_path)  # Вызов метода родительского класса для загрузки на Яндекс.Диск


