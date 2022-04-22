from django.urls import re_path, path
from . import views
from user.Views import userviews

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'users/import', views.findRandomUser),
    path('users', userviews.getAllUser),
    re_path(r'users/(?P<uuid>.*)', userviews.filterUser),
]
