# Generated by Django 2.2.5 on 2021-01-06 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_auto_20210106_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='conversations', to='users.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='conversations.Conversation'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='users.User'),
        ),
    ]
