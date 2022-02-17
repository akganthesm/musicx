import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/342a3f2ff01dfdcdbe9ab.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
[BOT FAST LIKE FAST AS FUCK]
┏━━━━━━━━━━━━━━━━━┓
┣★ OWNER    : [AKG_ANTHESM](https://t.me/AKG_ANTHESM)
┣★ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩  : [BACKCHODI POINT](https://t.me/CHOCO_AUTOBOT)
┗━━━━━━━━━━━━━━━━━┛

━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴊᴏɪɴ ʜᴇʀᴇ ғᴏʀ ᴜᴘᴅᴀᴛᴇs ❱ ➕", url=f"https://t.me/CHOCO_AUTOBOT")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
           photo=f"https://telegra.ph/file/342a3f2ff01dfdcdbe9ab.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
[BOT FAST LIKE FAST AS FUCK]
┏━━━━━━━━━━━━━━━━━┓
┣★ OWNER    : [AKG_ANTHESM](https://t.me/AKG_ANTHESM)
┣★ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩  : [BACKCHODI POINT](https://t.me/anthesm_support)
┗━━━━━━━━━━━━━━━━━┛

━━━━━━━━━━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/CHOCO_AUTOBOT")
                ]
            ]
        ),
    )


