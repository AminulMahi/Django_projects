# Generated by Django 4.2.5 on 2023-11-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_rename_url_main_f_url_main_g_url_main_l_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password1', models.IntegerField()),
                ('password2', models.IntegerField()),
            ],
        ),
    ]
