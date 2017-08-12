#coding=utf-8

from django.conf.urls import url
from view.views import *
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

urlpatterns = [
    # url(r'^test/$',test,{'offset':1}),    #方法一：字典传参
    # url(r'^test/(\w{1,3})/$',test),     #方法二：位置传参,\d表示匹配任何十进制数，\w表示匹配任何数字字母
    url(r'^test/(?P<offset>\w{1,3})/$',test),     #“？P”：为字符串匹配标识，{1,3}表示匹配1-3个，<offset>表示是参数
    url(r'foo/$',foo_bar,{'template_name':"foo.html"}),
    url(r'bar/$',foo_bar,{'template_name':"bar.html"}),
]

urlpatterns += [
    url(r'^about/$',TemplateView.as_view(template_name = 'about.html')),
    url(r'^go-to',RedirectView.as_view(url = 'https://docs.djangoproject.com')),
    url(r'^my_view',MyView.as_view()),
]
