import asyncio, os
from pyrogram import Client
from pyrogram.types import Message
from app import MY_CHANNEL_ID
from pyrogram.errors import ChatForwardsRestricted, FloodWait





async def forward_post(client:Client,message:Message):
    try:
        try:
            await message.copy(MY_CHANNEL_ID)
        except ChatForwardsRestricted:
            file = await message.download()
            caption = message.caption if message.caption else ""
            if message.document:
                await client.send_document(chat_id=MY_CHANNEL_ID, document=file, file_name=message.document.file_name, caption=caption)
            elif message.photo:
                await client.send_photo(chat_id=MY_CHANNEL_ID, photo=file, caption=caption)
            elif message.audio:
                await client.send_audio(chat_id=MY_CHANNEL_ID, audio=file, title = message.audio.title, file_name=message.audio.file_name, caption=caption)
            elif message.video:
                await client.send_video(chat_id=MY_CHANNEL_ID, video=file, caption=caption, file_name=message.video.file_name,)
            if os.path.exists(file): os.remove(file)
    except FloodWait as error:
        await asyncio.sleep(error.x)
        try:
            if os.path.exists(file): os.remove(file)
        except:
            pass
        await forward_post(client, message)



