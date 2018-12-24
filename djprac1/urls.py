from django.conf.urls import url
from . import views
from django.conf.urls import url,include
from django.contrib import admin

from .import views

app_name = "djprac1"


urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^(?P<blog_id>[0-9]+)', views.detail, name='blog_detail'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.catagory, name='blog_category'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag, name='blog_tag'),
    url(r'^search/$', views.search, name='blog_search'),
]