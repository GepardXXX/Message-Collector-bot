from aiogram.types import Message, ContentType

class JoinHandler():
    def __init__(self):
        self.content_types = ContentType.NEW_CHAT_MEMBERS  # Установка типа контента для обработки новых участников чата

    async def join_to_group(self, message: Message):
            # Метод для обработки добавления бота в группу и ответа на это событие
            if message.new_chat_members[0].id == 'bot_id':  # Проверка, что новый участник чата - это бот
                await message.answer("Спасибо, что добавили меня в группу! Теперь я буду собирать сообщения здесь.")
                # Отправка ответного сообщения с благодарностью и объявлением о начале сбора сообщений
