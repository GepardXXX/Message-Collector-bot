from aiogram.types import  Message
from aiogram.dispatcher.filters import Command
from ...keyboards import add_group_keyboard


class CommandStart(Command):
    def __init__(self):
        super().__init__('start')  # Вызов родительского класса Command
    
    async def start(self, message: Message):
        user_name = message.from_user.username
        if user_name == 'YourUserName':  # Проверка имени пользователя
            if not message.chat.type in ['group', 'supergroup', 'channel']: # Если чат не является группой, супергруппой или каналом
                await message.answer("Привет! Я бот для сбора сообщений из группы.\nЧтобы я мог собирать сообщения, добавь меня в свою группу и назначь администратором", reply_markup=add_group_keyboard)
                # Отправка ответного сообщения с приветствием и инструкцией, а также клавиатурой