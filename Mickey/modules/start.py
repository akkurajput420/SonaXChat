# Don't remove This Line From Here. Tg: @Dev_Arora_0981 | @DevArora0981
# Github :- Devarora-0981 | Devarora2604

import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from Mickey import OWNER, MickeyBot
from config import EMOJIOS, IMG, STICKER
from Mickey import MickeyBot
from Mickey.database.chats import add_served_chat
from Mickey.database.users import add_served_user
from Mickey.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


@MickeyBot.on_cmd(["start", "aistart"])
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ sтαятιиg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ sтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"<blockquote><b>๏ ʜᴇʏ,</b> ɪ ᴀᴍ {MickeyBot.name}</blockquote>\n<blockquote>➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.</blockquote>\n──────────────\n<blockquote>➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]</blockquote>\n<blockquote><b>||๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ||</b></blockquote>",
           # reply_markup=keyboard,
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@MickeyBot.on_cmd("help")
async def help(client: MickeyBot, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**<blockquote>ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!</blockquote>**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@MickeyBot.on_cmd("repo")
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@MickeyBot.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)



# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# AUTO_SLEEP = 5
# IS_BROADCASTING = False
# broadcast_lock = asyncio.Lock()


# @MickeyBot.on_cmd("rrepo") & filters.user(OWNER))
# async def broadcast_message(client, message):
#     global IS_BROADCASTING
#     bot_id = (await client.get_me()).id
#     clone_id = (await client.get_me()).id
#     user_id = message.from_user.id
#     if not await is_owner(clone_id, user_id):
#         await message.reply_text("You don't have permission to use this command on this bot.")
#         return
        
#     async with broadcast_lock:
#         if IS_BROADCASTING:
#             return await message.reply_text(
#                 "A broadcast is already in progress. Please wait for it to complete."
#             )

#         IS_BROADCASTING = True
#         try:
#             query = message.text.split(None, 1)[1].strip()
#         except IndexError:
#             query = message.text.strip()
#         except Exception as eff:
#             return await message.reply_text(
#                 f"**Error**: {eff}"
#             )
#         try:
#             if message.reply_to_message:
#                 broadcast_content = message.reply_to_message
#                 broadcast_type = "reply"
#                 flags = {
#                     "-pin": "-pin" in query,
#                     "-pinloud": "-pinloud" in query,
#                     "-nogroup": "-nogroup" in query,
#                     "-user": "-user" in query,
#                 }
#             else:
#                 if len(message.command) < 2:
#                     return await message.reply_text(
#                         "**Please provide text after the command or reply to a message for broadcasting.**"
#                     )
                
#                 flags = {
#                     "-pin": "-pin" in query,
#                     "-pinloud": "-pinloud" in query,
#                     "-nogroup": "-nogroup" in query,
#                     "-user": "-user" in query,
#                 }

#                 for flag in flags:
#                     query = query.replace(flag, "").strip()

#                 if not query:
#                     return await message.reply_text(
#                         "Please provide a valid text message or a flag: -pin, -nogroup, -pinloud, -user"
#                     )

                
#                 broadcast_content = query
#                 broadcast_type = "text"
            

#             await message.reply_text("**Started broadcasting...**")

#             if not flags.get("-nogroup", False):
#                 sent = 0
#                 pin_count = 0
#                 async for dialog in client.get_dialogs():
#                     chat_id = dialog.chat.id
#                     if chat_id == message.chat.id:
#                         continue
#                     try:
#                         if broadcast_type == "reply":
#                             m = await client.forward_messages(
#                                 chat_id, message.chat.id, [broadcast_content.id]
#                             )
#                         else:
#                             m = await client.send_message(
#                                 chat_id, text=broadcast_content
#                             )
#                         sent += 1
#                         await asyncio.sleep(20)

#                         if flags.get("-pin", False) or flags.get("-pinloud", False):
#                             try:
#                                 await m.pin(
#                                     disable_notification=flags.get("-pin", False)
#                                 )
#                                 pin_count += 1
#                             except Exception as e:
#                                 continue

#                     except FloodWait as e:
#                         flood_time = int(e.value)
#                         logger.warning(
#                             f"FloodWait of {flood_time} seconds encountered for chat {chat_id}."
#                         )
#                         if flood_time > 200:
#                             logger.info(
#                                 f"Skipping chat {chat_id} due to excessive FloodWait."
#                             )
#                             continue
#                         await asyncio.sleep(flood_time)
#                     except Exception as e:
                        
#                         continue

#                 await message.reply_text(
#                     f"**Broadcasted to {sent} chats and pinned in {pin_count} chats.**"
#                 )

#             if flags.get("-user", False):
#                 susr = 0
#                 async for dialog in client.get_dialogs():
#                     chat_id = dialog.chat.id
#                     try:
#                         if broadcast_type == "reply":
#                             m = await client.forward_messages(
#                                 user_id, message.chat.id, [broadcast_content.id]
#                             )
#                         else:
#                             m = await client.send_message(
#                                 user_id, text=broadcast_content
#                             )
#                         susr += 1
#                         await asyncio.sleep(20)

#                     except FloodWait as e:
#                         flood_time = int(e.value)
#                         logger.warning(
#                             f"FloodWait of {flood_time} seconds encountered for user {user_id}."
#                         )
#                         if flood_time > 200:
#                             logger.info(
#                                 f"Skipping user {user_id} due to excessive FloodWait."
#                             )
#                             continue
#                         await asyncio.sleep(flood_time)
#                     except Exception as e:
                        
#                         continue

#                 await message.reply_text(f"**Broadcasted to {susr} users.**")

#         finally:
#             IS_BROADCASTING = False

