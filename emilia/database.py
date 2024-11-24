from loguru import logger
from peewee import *

from emilia.config import DB_PATH

database = SqliteDatabase(DB_PATH)


class Chat(Model):
    """Модель чата в базе данных"""

    chat_id = BigIntegerField()
    owner_id = BigIntegerField(default=None, null=True)
    rules = TextField(default=None, null=True)
    greeting = TextField(default=None, null=True)
    prefix_disable = BooleanField(default=False)

    class Meta:
        database = database
        db_table = "chats"


class ChatMember(Model):
    """Модель пользователя чата в базе данных"""

    member_id = BigIntegerField()
    chat_id = BigIntegerField()
    rank = SmallIntegerField(default=1)
    nickname = TextField(default=None, null=True)

    class Meta:
        database = database
        db_table = "chat_members"


def create_tables():
    """Создать таблицы в базе данных"""

    Chat.create_table()
    ChatMember.create_table()
    logger.info("База данных создана")
