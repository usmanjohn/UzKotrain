from django.core.management.base import BaseCommand
from bot.models import NotificationTemplate

class Command(BaseCommand):
    help = 'Creates notification templates for Telegram'

    def handle(self, *args, **kwargs):
        templates = [
            {
                'content_type': 'topic',
                'template': "New Topic by <b>{topic_author}</b>:\n\n<b>{topic_title}</b>\n\n{topic_body}\n\nCreated on: {topic_pub_date}\n\n<a href='{url}'>Read more</a>"
            },
            {
                'content_type': 'podcast',
                'template': "New Podcast: <b>{title}</b>\n\nBy: {audio_uploader}\n\n{description}\n\nReleased on: {date_published}\n\n<a href='{url}'>Listen now</a>"
            },
            {
                'content_type': 'tutor',
                'template': "New Tutoring Session: <b>{title}</b>\n\nBy: {author}\n\n{description}\n\nScheduled on: {date}\n\n<a href='{url}'>View details</a>"
            },
        ]

        for template_data in templates:
            NotificationTemplate.objects.get_or_create(
                content_type=template_data['content_type'],
                defaults={'template': template_data['template']}
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully created notification templates'))