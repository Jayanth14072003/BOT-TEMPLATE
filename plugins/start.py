#Coded by KA18 the @legend580 💛❤️

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, CallbackQuery

from bot import Bot
from config import *
from Script import script

@Bot.on_message(filters.command('start') & filters.private)
async def start_command(client: Client, message: Message):
    a = await message.reply_text("Processing....")
    await delete(a)
    await client.send_message(
            text = script.START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            disable_web_page_preview = True,
            quote = True
        )
