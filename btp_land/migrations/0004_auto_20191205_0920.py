# Generated by Django 2.2 on 2019-12-05 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btp_land', '0003_auto_20191204_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='btp_land.Project'),
        ),
    ]
