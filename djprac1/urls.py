from django.conf.urls import url
from . import views
from django.conf.urls import url,include
from django.contrib import admin

from .import views

app_name = "djprac1"


urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^(?P<blog_id>[0-9]+)', views.detail, name='blog_detail'),
]