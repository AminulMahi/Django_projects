# Generated by Django 4.2.5 on 2023-10-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_user_data_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='video',
            field=models.ImageField(default=1, upload_to='video/'),
            preserve_default=False,
        ),
    ]
