from loguru import logger
from vk_api.bot_longpoll import VkBotEventType

from emilia.config import BOT_PREFIXES
from emilia.handlers.common import ping
from emilia.utils import db_utils

# Обработчики которые работают и в лс и в чате
common_handlers = {}

# Обработчики которые работают только в чате
chat_handlers = {}


def add_handler(command, handler, out):
    """Добавить обработчик"""
    ...


def remove_handler(command):
    """Удалить обработчик"""
    ...


def processing_handlers(vk, event):
    """Обработать событие если есть обработчик"""
    logger.debug(f"Событие: {event.raw}")

    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.message
        peer_id = message.peer_id
        text = message.text
        command = text.split()[0].lower()

        if any(text.startswith(prefix) for prefix in BOT_PREFIXES):
            command = command[1:]

        if command in common_handlers:
            common_handlers[command](vk, event)
        elif command in chat_handlers and peer_id > 2000000000:
            chat_handlers[command](vk, event)
