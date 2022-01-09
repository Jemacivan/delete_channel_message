from aiogram import Dispatcher, Bot
from aiogram.bot.api import TelegramAPIServer

from configure import Config

config = Config()
config.read()


bot = Bot(
    token=config.token, 
    server=TelegramAPIServer.from_base(config.telegram_bot_api_server)
)
dp = Dispatcher(bot)