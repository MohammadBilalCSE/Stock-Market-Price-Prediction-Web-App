# Generated by Django 5.0.2 on 2024-05-03 13:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smpapp1', '0006_postform'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostForm',
            new_name='Post',
        ),
    ]
