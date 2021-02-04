""" defines URL for users"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # include default auth urls
    path('', include('django.contrib.auth.urls'')),
]