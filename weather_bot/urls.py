from django.contrib import admin
from django.urls import path, include

from .views import CallbackView

urlpatterns = [
    path('callback/', CallbackView.as_view(), name='callback')
]
