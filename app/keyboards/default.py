from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создание кнопки с текстом "Добавить меня в группу" и ссылкой на добавление бота в группу через URL-ссылку
add_group_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Добавить меня в группу', url='https://t.me/your_bot_name?startgroup=hbase')
)