from django.db import models
from django.contrib.auth import get_user_model


class ViberUser(models.Model):
    viber_id = models.CharField(max_length=13)
    name = models.CharField(max_length=75, null=True, blank=True)
    avatar = models.URLField(null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True)
    language = models.CharField(max_length=2, null=True, blank=True)
    primary_device_os = models.CharField(max_length=48, null=True, blank=True)
    api_version = models.PositiveSmallIntegerField(null=True, blank=True)
    viber_version = models.CharField(max_length=24, null=True, blank=True)
    device_type = models.CharField(max_length=48, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
