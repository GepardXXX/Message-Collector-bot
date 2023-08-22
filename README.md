# Message collector
[![GitHub license](https://img.shields.io/github/license/GepardXXX/Message-Collector-bot)](https://github.com/GepardXXX/Message-Collector-bot/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3x/)
![GitHub last commit](https://img.shields.io/github/last-commit/GepardXXX/Message-Collector-bot)
![GitHub repo size](https://img.shields.io/github/repo-size/GepardXXX/Message-Collector-bot)
![GitHub Watchers](https://img.shields.io/github/watchers/GepardXXX/Message-Collector-bot?style=social)


Этот проект представляет собой Telegram-бота, который может собирать сообщения из группы и сохранять их на Yandex Disk. 

## Требования
Для корректной работы проекта необходимо наличие следующих программ, библиотек и версий:

- Python 3.10
- Зависимости, указанные в `requirements.txt`


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

### Модули-обработчики в папке `handlers`
- `commands/` содержит обработчики команд, например, команды `/start`, которая инициализирует бота.
- `collectors/` содержит обработчики для сбора и сохранения различных типов медиа-контента.
- `join_handler/` содержит обработчик для добавления бота в группу.

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
### Примеры использования
- Чтобы активировать бота, добавьте его в группу и назначьте администратором.
- Бот будет собирать различные типы медиа-контента, такие как фотографии, видео, аудио и другие, и сохранять их на Yandex Disk.
  
## Лицензия
Этот проект распространяется под лицензией [GPLv3](). Вы можете найти полный текст лицензии в файле LICENSE. При использовании или распространении этого кода, пожалуйста, убедитесь, что вы указали авторство:
<span style="color:gray">**Copyright 2023 GepardXXX**</span>


## Связь
Если у вас возникли вопросы, предложения или проблемы с проектом, не стесняйтесь связаться со мной через:

- [GitHub](https://github.com/GepardXXX)
- [Telegram](https://t.me/GepardXXX)


## Запуск в Docker-контейнере (по желанию)
Если вы предпочитаете использовать Docker, вы можете легко развернуть проект в контейнере. Для этого выполните следующие шаги:

1. Установите Docker на вашу систему.
2. Склонируйте репозиторий: `git clone https://github.com/GepardXXX/Message-Collector-bot.git`
3. Перейдите в каталог проекта: `cd Message-Collector-bot`
4. Соберите Docker-образ: `docker build -t message-collector-bot .`
5. Запустите контейнер: `docker run -d message-collector-bot`