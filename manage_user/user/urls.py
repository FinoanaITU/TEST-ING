from django.urls import re_path, path
from . import views
from user.Views import userviews

urlpatterns = [
    re_path(r'^$', views.index),
    path('users/import', views.findRandomUser),
    re_path(r'^users/(?P<uuid>.*)', userviews.filterUser),
    re_path(r'users', userviews.getAllUser),
]
