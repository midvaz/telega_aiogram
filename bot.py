import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from main_menu.handlers import main_menu

from tgbot.config import load_config
from tgbot.data_base import connect
logger = logging.getLogger(__name__)

#вызов функции по открытию бд
def create_pool(user, password, database, host, echo):
    try:
        connect()
    except:
        raise NotImplementedError  

#основная асинхронная функция 
async def main():
    logging.basicConfig(
        # debug if need see all logs
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting bot")
    config = load_config("bot.ini")

    storage = MemoryStorage()
    pool = create_pool(
        user=config.db.user,
        password=config.db.password,
        database=config.db.database,
        host=config.db.host,
        echo=False,
    )

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=storage)


    main_menu(dp)


    # start
    try:
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    asyncio.run(main())
