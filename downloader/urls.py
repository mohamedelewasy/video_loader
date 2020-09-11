from django.urls import path, include
from . import views

app_name = 'downloader'

urlpatterns = [
    path('', views.fun),
]