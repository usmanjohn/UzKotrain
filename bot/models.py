from django.db import models

class NotificationTemplate(models.Model):
    CONTENT_TYPES = (
        ('topic', 'Topic'),
        ('podcast', 'Podcast'),
        ('tutor', 'Tutor'),
    )
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    template = models.TextField()

    def __str__(self):
        return f"Template for {self.get_content_type_display()}"