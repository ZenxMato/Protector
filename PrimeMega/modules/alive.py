import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from PrimeMega.events import register
from PrimeMega import telethn as tbot


PHOTO = "https://telegra.ph/file/2de22d648488aeb0d533c.jpg"

@register(pattern=("/alive"))
async def awake(event):
  PRIME = f"**Hello Kids [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Prime Mega.** \n\n"
  PRIME += "🔅 **I'm Working Properly** \n\n"
  PRIME += f"🔅 **My Master : [Lord](https://t.me/You_Bitchhh)** \n\n"
  PRIME += f"🔅 **Library Version :** `{telever}` \n\n"
  PRIME += f"🔅 **Telethon Version :** `{tlhver}` \n\n"
  PRIME += f"🔅 **Pyrogram Version :** `{pyrover}` \n\n"
  PRIME += "**Thanks For Using Swain Robot**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/ProtectorX_Bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/KataSwain")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PRIME,  buttons=BUTTON)
