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

            if text != "":
                prefix = text[0]
                command = text[1:].strip()

                if prefix in BOT_PREFIXES and command in handlers:
                    handlers[command](vk, event)
    except Exception as e:
        logger.error(f"Получена ошибка при обработке события: {e}")
