# Generated by Django 4.2.5 on 2023-10-16 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_user_data_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_data1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]