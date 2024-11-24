import time
from threading import Thread

from loguru import logger
from requests.exceptions import ReadTimeout
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.vk_api import VkApiGroup

from emilia.handlers import processing_handlers


def start_bot(bot_token, bot_id):
    """Запустить бота"""
    try:
        vk_session = VkApiGroup(token=bot_token)
        vk = vk_session.get_api()
        longpoll = VkBotLongPoll(vk_session, bot_id)
    except Exception as e:
        logger.error(f"Получена ошибка при авторизации: {e}")

    group_info = vk.groups.getById(group_id=bot_id)[0]
    logger.info(f"Бот запущен ({group_info['name']}, {bot_id})")

    while True:
        try:
            for event in longpoll.listen():
                Thread(
                    target=processing_handlers,
                    args=(
                        vk,
                        event,
                    ),
                    daemon=True,
                ).start()
        except ReadTimeout:
            logger.error(f"Получена ошибка соединения. Засыпаю на 5 секунд.")
            time.sleep(5)
        except Exception as e:
            logger.error(f"Получена ошибка при прослушивании: {e}")
