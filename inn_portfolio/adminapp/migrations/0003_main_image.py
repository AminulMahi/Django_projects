# Generated by Django 4.2.5 on 2023-10-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_main_l_name_main_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]