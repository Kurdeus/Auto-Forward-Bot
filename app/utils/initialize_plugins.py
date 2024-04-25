from pyrogram import filters, handlers
from app.plugins import forward_post
from app import bot, TARGET_CHANNEL_ID

bot.add_handler(handlers.MessageHandler(forward_post, filters=filters.chat([TARGET_CHANNEL_ID])))
