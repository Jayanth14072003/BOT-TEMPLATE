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

@Bot.on_message(filters.command('auth') & filters.user(OWNER_ID))
async def add_auth(bot, update):
    cmd = update.command
    if len(cmd) == 1:
        return await update.reply(text = "Send the command properly.\nExample: <code>/auth 1061576483</code>")
    elif len(cmd) == 2:
        try:
            auth_id = int(cmd[1].strip())
            await update.reply(text = f"<b>New User Adde🎉.\n User ID - {auth_id}</b>")
        except:
            await update.reply(text = "Invalid User ID, please chech again and resend.")
