# Generated by Django 2.2.5 on 2020-12-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='host',
        ),
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancled', 'Cancled')], default='pending', max_length=12),
        ),
    ]
