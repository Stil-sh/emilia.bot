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
    ...
