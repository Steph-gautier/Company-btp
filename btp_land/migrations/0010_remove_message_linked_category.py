# Generated by Django 2.2 on 2019-12-05 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btp_land', '0009_message_linked_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='linked_category',
        ),
    ]
