#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
import datetime
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery, datetime):
    data = query.data
    dateday = [1]
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='https://t.me/link_serials'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://t.me/dj_serials_bot'>Click here</a>\n○ Channel : @link_serials\n○ Support Group : @dj_serials_bot</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
            
    if query.data == "ystdy":
        dateday.clear()
        xx = datetime.now()-timedelta(1)
        x = xx.strftime("%d-%m-%Y")
        dateday.append(x)
        await query.message.edit_text(
            text="Dete set to Yesterday.."
        )
        
    elif query.data == "tdy":
        dateday.clear()
        yy = datetime.now()
        y = yy.strftime("%d-%m-%Y")
        dateday.append(y)
        await query.message.edit_text(
            text="Dete set to Today.."
        )
    elif query.data == "tmr":
        dateday.clear()
        zz = datetime.now()+timedelta(1)
        z = zz.strftime("%d-%m-%Y")
        dateday.append(z)
        await query.message.edit_text(
            text="Dete set to Tomorrow.."
        )
    else:
        pass
    return dateday
