import os
import asyncio
from telegram import Bot
from kotrain.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID, BASE_URL
from django.urls import reverse
from telegram.constants import ParseMode




bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_topic_to_telegram_async(topic):
    url = BASE_URL + reverse('topic-detail', args=[topic.pk])
    author_url = BASE_URL + reverse('profile', args=[topic.topic_author.username])
    message = (
        f"<b>New Tutorial:</b> <a href='{author_url}'>{topic.topic_author.username}</a> posted a new tutorial: \n\n"
        f"<b>Title:</b> <a href='{url}'>{topic.topic_title}</a>\n\n"
        f"<b>Description:</b>{topic.topic_body[:100]}...\n\n"
        f"<b>Category:</b>{topic.topic_category[:100]}...\n\n"
        f"<a href='{url}'>Go to tutorial</a>"
    )
    await bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message, parse_mode = ParseMode.HTML)

def send_topic_to_telegram(topic):
    asyncio.run(send_topic_to_telegram_async(topic))