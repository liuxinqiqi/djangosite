#coding=utf-8

from django.conf.urls import url
from myapp.views import *

urlpatterns = [
    url(r'^first/$',first),
    url(r'^bs/$',bs),
    url(r'^test/$',test),
    url(r'^template/$',temp),
    url(r'^hello/$',hello),
    url(r'^meta/$',display_meta),
    url(r'^tag/$',tag),  # 标签
    url(r'^filter/$',fil), # 过滤器

    url(r'^base/$',base,name = 'base') , #  模板的继承
    url(r'^include/$',nav), # nav.html中有用全局变量
    url(r'static/$',load),# 静态文件的加载  image
]
