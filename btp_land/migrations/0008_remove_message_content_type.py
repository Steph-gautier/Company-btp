# Generated by Django 2.2 on 2019-12-05 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btp_land', '0007_auto_20191205_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='content_type',
        ),
    ]
