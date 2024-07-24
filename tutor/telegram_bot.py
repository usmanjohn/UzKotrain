import os
import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from kotrain.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID, BASE_URL
from django.urls import reverse
from django.utils.html import strip_tags



bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_topic_to_telegram_async(tutor):
    url = BASE_URL + reverse('tutor-detail', args=[tutor.pk])
    author_url = BASE_URL + reverse('profile', args=[tutor.author.username])
    description = strip_tags(tutor.description)[:100]
    category = strip_tags(tutor.category)[:100]
    message = (
        f"<b>New Tutorial:</b> <a href='{author_url}'>{tutor.author.username}</a> posted a new tutorial: \n\n"
        f"<b>Title:</b> <a href='{url}'>{tutor.title}</a>\n\n"
        f"<b>Description:</b>{description}...\n\n"
        f"<b>Category:</b>{category}...\n\n"
        f"<a href='{url}'>Go to tutorial</a>"
    )

    await bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message, parse_mode=ParseMode.HTML)

def send_topic_to_telegram(tutor):
    asyncio.run(send_topic_to_telegram_async(tutor))