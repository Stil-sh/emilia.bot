from peewee import *
from loguru import logger
from emilia.config import DB_PATH

database = SqliteDatabase(DB_PATH)


class Chat(Model):
    """Модель чата в базе данных"""
    chat_id = BigIntegerField()
    owner_id = BigIntegerField(default=None)
    rules = TextField(default=None)
    greeting = TextField(default=None)

    class Meta:
        database = database


class ChatMember(Model):
    """Модель пользователя чата в базе данных"""
    member_id = BigIntegerField()
    chat_id = BigIntegerField()
    rank = SmallIntegerField(default=1)
    nickname = TextField(default=None)

    class Meta:
        database = database


def create_tables():
    """Создать таблицы в базе данных"""
    Chat.create_table()
    ChatMember.create_table()
    logger.info("База данных создана")
