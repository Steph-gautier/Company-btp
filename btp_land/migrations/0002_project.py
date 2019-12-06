# Generated by Django 2.2 on 2019-12-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btp_land', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
            ],
        ),
    ]