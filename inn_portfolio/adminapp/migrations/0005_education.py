# Generated by Django 4.2.5 on 2023-10-31 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=100)),
                ('u_title', models.CharField(max_length=100)),
                ('u_subject', models.CharField(max_length=100)),
                ('u_gpa', models.IntegerField()),
                ('u_date', models.DateField()),
            ],
        ),
    ]