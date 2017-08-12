#coding=utf-8

from django.conf.urls import url
from myapp.views import *


urlpatterns = [
    url(r'^$', index, name = 'index'),
    # url(r'^$', index, name = 'index'),
    url(r'^reg/',reg, name = 'reg'),
    url(r'^tag/',tag, name = 'tag'),
    url(r'^login/', login, name = 'login'),
    url(r'^logout$', logout, name = 'logout'),
    url(r'^article/$', article, name = 'article'),
    url(r'^category/$', category, name = 'category'),
    url(r'^archive/$', archive, name = 'archive'),
    # url(r'^comment/$', comment, name = 'comment'),
    url(r'^comment/post$', comment_post, name = 'comment_post'),

]
