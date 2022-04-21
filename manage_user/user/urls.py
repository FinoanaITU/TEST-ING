from importlib.resources import path
from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^users/import', views.findRandomUser),
]
