from emilia.database import create_tables
from emilia.bot import start_bot
from emilia.config import BOT_TOKEN, BOT_ID


if __name__ == "__main__":
    create_tables()
    start_bot(BOT_TOKEN, BOT_ID)
