# Generated by Django 4.2.5 on 2023-10-28 01:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0012_rename_userprofile_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
    ]
