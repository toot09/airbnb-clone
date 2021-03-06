# Generated by Django 2.2.5 on 2020-12-29 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('reservations', '0002_auto_20201229_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.Room'),
        ),
    ]
