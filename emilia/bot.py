import time
from threading import Thread

from loguru import logger
from requests.exceptions import ReadTimeout
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.vk_api import VkApiGroup

from emilia.handlers import handle_event


def start_bot(bot_token, bot_id):
    """Запустить бота"""
    try:
        vk_session = VkApiGroup(token=bot_token)
        vk = vk_session.get_api()
        longpoll = VkBotLongPoll(vk_session, bot_id)
    except Exception as e:
        logger.error(f"Получена ошибка при авторизации: {e}")

    logger.info("Бот запущен")

    while True:
        try:
            for event in longpoll.listen():
                Thread(
                    target=handle_event,
                    args=(
                        vk,
                        event,
                    ),
                    daemon=True,
                ).start()
        except KeyboardInterrupt:
            logger.info("Завершение работы по команде")
            break
        except ReadTimeout:
            logger.error(f"Получена ошибка соединения. Засыпаю на 5 секунд.")
            time.sleep(5)
        except Exception as e:
            logger.error(f"Получена ошибка при прослушивании: {e}")
