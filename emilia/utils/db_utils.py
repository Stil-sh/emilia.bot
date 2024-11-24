from loguru import logger
from peewee import DoesNotExist

from emilia.database import Chat, ChatMember


def reg_chat(chat_id):
    try:
        Chat.get(chat_id=chat_id)
    except DoesNotExist:
        Chat.create(chat_id=chat_id)
        logger.info(f"Новый чат зарегистрирован {chat_id}")
