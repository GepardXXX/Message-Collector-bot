import os
import datetime
from aiogram.types import ContentType, Message, ChatType
from aiomisc.io import async_open  
from utils import YandexDisk  # Подключаем необходимые модули и библиотеки


class MediaCollector():
    def __init__(self):
        # Определение поддерживаемых типов контента и типов чатов
        self.content_types = [ContentType.VOICE, ContentType.PHOTO, ContentType.VIDEO, ContentType.DOCUMENT, ContentType.AUDIO]
        self.chat_type = [ChatType.GROUP, ChatType.SUPERGROUP]

    async def collect_media_message(self, message: Message):
        content_type = message.content_type

        # Определение типа медиа и получение file_id
        if content_type == ContentType.PHOTO:
            file_id = message.photo[-1].file_id
        elif content_type == ContentType.VIDEO:
            file_id = message.video.file_id
        elif content_type == ContentType.AUDIO:
            file_id = message.audio.file_id
        elif content_type == ContentType.DOCUMENT:
            file_id = message.document.file_id
        elif content_type == ContentType.VOICE:
            file_id = message.voice.file_id

        if file_id:
            await self.download_and_save_media(message, file_id)  # Вызов функции для сохранения медиа

    @staticmethod
    def get_extension(file):
        return os.path.splitext(file.file_path)[1]  # Получение расширения файла из пути

    def get_user_name(self, message: Message):
        user = message.from_user
        return user.username if user.username else str(user.id)  # Получение имени пользователя или ID

    @staticmethod
    def get_formatted_time():
        current_time = datetime.datetime.now()
        return current_time.strftime("%Y-%m-%d %H-%M-%S-%f")  # Получение текущего времени в заданном формате

    def generated_file_name(self, message: Message, extension):
        user_name = self.get_user_name(message)
        formatted_time = self.get_formatted_time()
        return f'{user_name}_{formatted_time}{extension}'  # Создание уникального имени файла

    async def download_and_save_media(self, message: Message, file_id):
        if file_id:
            save_file = await message.bot.download_file_by_id(file_id)
            file = await message.bot.get_file(file_id)
            extension = self.get_extension(file)
            file_name = self.generated_file_name(message, extension)

            async with async_open(file_name, 'wb') as f:
                await f.write(save_file.getvalue())  # Сохранение файла на диск

            await self.upload_to_yandex_disk(
                file_path=f'your/path{file_name}', file_name=file_name)

    async def upload_to_yandex_disk(self, file_name, file_path):
        await YandexDisk().save_content(file_name, file_path)  # Вызов функции для сохранения на Яндекс.Диск
        os.remove(file_name)  # Удаление временного файла после загрузки на Яндекс.Диск