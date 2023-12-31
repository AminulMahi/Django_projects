# Generated by Django 4.2.5 on 2023-11-01 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_awards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tools', models.ImageField(upload_to='images/')),
                ('workflow', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='u_gpa',
            field=models.FloatField(),
        ),
    ]
