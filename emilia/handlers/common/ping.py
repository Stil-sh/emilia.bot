import time

from emilia.config import EMOJI
from emilia.utils import vk_utils


def get_ping(vk, event):
    pingtime = round(time.time() - event['date'], 2)
    message = f"{EMOJI['good']} Обработано за {pingtime}с."
    vk_utils.send_message(vk, event.peer_id, message)
