#Coded by KA18 the @legend580 💛❤️

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os, time
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
    await a.delete()
    await client.send_message(
        	chat_id=message.chat.id,
            text = script.START_MSG.format(message.from_user.mention if message.from_user else message.chat.title),
            disable_web_page_preview = True
        )
