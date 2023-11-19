# Generated by Django 4.2.5 on 2023-10-31 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_main_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('sub_heading', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=600)),
                ('date', models.DateField()),
            ],
        ),
    ]