# Generated by Django 4.2.5 on 2023-10-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_user_data_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
