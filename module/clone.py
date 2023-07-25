from main import API_ID, API_HASH
from pyromek import *
import os
import re
import asyncio
import time

OWNER_ID = [1207941747]


@Client.on_message(filters.user(OWNER_ID) & filters.command("clone", "."))
async def clone(client, message):
    chat = message.chat
    text = await message.reply("Clone")
    cmd = message.command
    try:
        phone = message.command[1]
    except IndexError:
        pass
    try:
        await text.edit("Booting Your Client")
        # change this Directory according to your repo
        client = Client(name="Hakutaka", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="module"))
        await client.start()
        user = await client.get_me()
        await message.reply(f"Your Client Has Been Successfully As {user.first_name} ✅.")
    except Exception as e:
        await message.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
