from aiogram import Dispatcher
from .handlers import commands, join_handler, collectors


# Функция для настройки обработчиков сообщений и событий бота
def setup(dp: Dispatcher):
    # Регистрация обработчика команды /start
    dp.register_message_handler(commands.CommandStart().start, commands.CommandStart())
    # Регистрация обработчика сбора медиа-сообщений
    dp.register_message_handler(collectors.MediaCollector().collect_media_message, content_types=collectors.MediaCollector().content_types, chat_type=collectors.MediaCollector().chat_type)
    # Регистрация обработчика сбора текстовых сообщений
    dp.register_message_handler(collectors.TextCollector().collect_text_message, content_types=collectors.TextCollector().content_types, chat_type=collectors.TextCollector().chat_type)
     # Регистрация обработчика события добавления бота в группу
    dp.register_message_handler(join_handler.JoinHandler().join_to_group, content_types=join_handler.JoinHandler().content_types)

