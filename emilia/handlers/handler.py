from loguru import logger


def handle_event(vk, event):
    """Обработать событие"""
    try:
        logger.debug(f"Новое событие: {event.raw}")
    except Exception as e:
        logger.error(f"Получена ошибка при обработке события: {e}")
