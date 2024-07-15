import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from Fitnes_bot.bot.handlers import main_router
from Fitnes_bot.bot.middlewares import CustomMiddleware

TOKEN = "7414985055:AAFDGuISpRBBAAhXRspyaTIqPzWOYHQ2Tcg"

dp = Dispatcher()

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(*[main_router])
    dp.update.middleware(CustomMiddleware())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())