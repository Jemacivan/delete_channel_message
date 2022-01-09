from datetime import datetime as dt

from aiogram import types
from aiogram.types.message import ContentType

from load import dp, bot, config


@dp.message_handler(content_types=[ContentType.ANY])
async def delete_msg(message: types.Message):
    if config.enable_filter:
        if message.chat.id not in config.allowed_chats:
            return

    if message.from_user.id == 136817688:
        try:
            await message.delete()

            if config.enable_logging:
                await bot.send_message(
                    config.logging_chat,
                    ("Chat: {chat}\n"
                    "Message text: {msg_text}\n"
                    "Time: {time}"
                    ).format(
                        chat=message.chat.title,
                        msg_text=str(message.text),
                        time=dt.strftime(dt.now(), "%m/%d/%Y %H:%M:%S")
                    )
                )
        except Exception:
            pass