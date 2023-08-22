# Message collector
[![GitHub license](https://img.shields.io/github/license/GepardXXX/Message-Collector-bot)](https://github.com/GepardXXX/Message-Collector-bot/blob/main/LICENSE)

Этот проект представляет собой Telegram-бота, который может собирать сообщения из группы и сохранять их на Yandex Disk. 

## Структура проекта
```
my_bot_project/
├── app/
│   ├── __init__.py
│   ├── bot.py
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── commands/
│   │   │   ├── __init__.py
│   │   │   ├── start.py
│   │   ├── collectors/
│   │   │   ├── __init__.py
│   │   │   ├── media_collector.py
│   │   │   ├── text_collector.py
│   │   ├── join_handler/
│   │   │   ├── __init__.py
│   │   │   ├── join_to_group.py
├── config/
│   ├── __init__.py
│   ├── settings.py
├── utils/
│   ├── __init__.py
│   ├── yandex_disk.py
├── main.py
└── requirements.txt
```

## Описание

- `app/` содержит основной код бота и его обработчики.
- `config/` содержит настройки проекта, такие как токены и параметры.
- `utils/` содержит вспомогательные модули, например, для взаимодействия с Yandex Disk.
- `main.py` - точка входа в приложение.

## Использование

1. Установите зависимости, указанные в `requirements.txt`, с помощью команды:

   ```
   pip install -r requirements.txt
   ```

2. Создайте файл `config/settings.py` и добавьте необходимые настройки, такие как токены для __Telegram__ и __Yandex Disk__.
3. Запустите бота, выполните:
   ```
   python main.py
   ```
## Лицензия


