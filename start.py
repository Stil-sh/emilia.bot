from emilia.bot import start_bot
from emilia.config import BOT_TOKEN, BOT_ID
from loguru import logger


if __name__ == "__main__":
    start_bot(BOT_TOKEN, BOT_ID)
