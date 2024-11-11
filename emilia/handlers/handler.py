import time

from emilia.handlers.common import ping
from emilia.config import BOT_PREFIXES

from loguru import logger
from vk_api.bot_longpoll import VkBotEventType


handlers = {
    "пинг": ping.get_ping
}


def handle_event(vk, event):
    """Обработать событие"""
    try:
        logger.debug(f"Новое событие: {event.raw}")

        if event.type == VkBotEventType.MESSAGE_NEW:
            event = event.message
            text = event.text.lower()

            if text != "" and text[0] in BOT_PREFIXES and text[1:] in handlers:
                handlers[text[1:]](vk, event)
    except Exception as e:
        logger.error(f"Получена ошибка при обработке события: {e}")
