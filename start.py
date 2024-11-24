from emilia.bot import start_bot
from emilia.config import BOT_ID, BOT_TOKEN
from emilia.database import create_tables

if __name__ == "__main__":
    create_tables()
    start_bot(BOT_TOKEN, BOT_ID)
