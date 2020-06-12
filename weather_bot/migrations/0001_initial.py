# Generated by Django 3.0.7 on 2020-06-12 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ViberUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viber_id', models.CharField(max_length=13)),
                ('name', models.CharField(max_length=75)),
                ('avatar', models.URLField()),
                ('country', models.CharField(max_length=2)),
                ('language', models.CharField(max_length=2)),
                ('primary_device_os', models.CharField(max_length=48)),
                ('api_version', models.PositiveSmallIntegerField()),
                ('viber_version', models.CharField(max_length=24)),
                ('device_type', models.CharField(max_length=48)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
