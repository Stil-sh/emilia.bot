from loguru import logger
from vk_api.bot_longpoll import VkBotEventType

from emilia.config import BOT_PREFIXES
from emilia.handlers.common import ping
from emilia.utils import db_utils

handlers = {"пинг": ping.get_ping}


def handle_event(vk, event):
    """Обработать событие"""
    try:
        logger.debug(f"Новое событие: {event.raw}")

        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                chat_id = event.chat_id
                db_utils.reg_chat(chat_id)

            event = event.message
            text = event.text.lower()

            if text != "":
                prefix = text[0]
                command = text[1:].strip()

                if prefix in BOT_PREFIXES and command in handlers:
                    handlers[command](vk, event)
    except Exception as e:
        logger.error(f"Получена ошибка при обработке события: {e}")
