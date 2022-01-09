#!/usr/bin/env python3
import logging

from aiogram import executor

import handlers
from load import bot, dp, config


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger("Bot")

WEBAPP_HOST = config.ip
WEBAPP_PORT = config.port

WEBHOOK_HOST = f'http://{WEBAPP_HOST}:{WEBAPP_PORT}'
WEBHOOK_PATH = f'/bot{config.token}/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

async def on_startup(dp):
    await bot.set_webhook(url=WEBHOOK_URL)


async def on_shutdown(dp):
    await bot.delete_webhook()

if config.use_webhook:
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        skip_updates=False,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )
else:
    executor.start_polling(dp, skip_updates=False)