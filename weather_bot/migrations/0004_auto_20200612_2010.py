# Generated by Django 3.0.7 on 2020-06-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_bot', '0003_auto_20200612_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='viberuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='viberuser',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
