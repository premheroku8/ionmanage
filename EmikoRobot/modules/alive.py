import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/7f8647c8016634aae1d42.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴀᴋᴜ ʏᴜɪɪ ʀᴏʙᴏᴛ.** \n\n"
  TEXT += "✘ **ᴀᴋᴜ ʜɪᴅᴜᴘ ᴅᴀɴ ᴀᴋᴜ ɴʏᴀᴛᴀ** \n\n"
  TEXT += f"✘ **ᴍʏ ʟᴏʀᴅ : [ ʏᴜɪɪ](https://t.me/onlybionn)** \n\n"
  TEXT += f"✘ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"✘ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"✘ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**ᴛᴇʀɪᴍᴀᴋᴀsɪʜ sᴜᴅᴀʜ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴋᴜ ᴅɪ sɪɴɪ 🔥**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/YuiichiroManage_Bot?start=help"), Button.url("ᴜᴘᴅᴀᴛᴇ", "https://t.me/zennihhh")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
