#Coded by KA18 the @legend580 💛❤️

import pyrogram
from bot import Bot
import time
import asyncio
from config import *
from datetime import datetime, timedelta
from pyrogram.types import Message, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    else:
        pass
