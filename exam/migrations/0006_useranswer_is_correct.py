# Generated by Django 5.0.6 on 2024-07-05 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_testattempt_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]