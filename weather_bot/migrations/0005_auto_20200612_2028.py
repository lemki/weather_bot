# Generated by Django 3.0.7 on 2020-06-12 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_bot', '0004_auto_20200612_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viberuser',
            name='name',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
