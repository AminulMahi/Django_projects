# Generated by Django 4.2.5 on 2023-09-30 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='message',
            new_name='messages',
        ),
    ]
