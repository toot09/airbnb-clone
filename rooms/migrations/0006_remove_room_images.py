# Generated by Django 2.2.5 on 2020-12-28 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_room_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='images',
        ),
    ]
