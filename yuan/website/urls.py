#coding=utf-8
"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from website import views


"""
url() 共四个参数
1. r'^admin/'：正则表达式
2. admin.site.urls : 调用这个方法去实现正则表达式
3. {'offset':"ouguan"} ： 参数，给views中传参，传参有两种方式

在本 urls 中存放的都是与系统有直接相关的urls文件，其余的都转为 app....include.. 要在相应的app文件中
写 urls文件内容
"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lol/$',views.home,name = 'home'),
    url(r'^time/$',views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$',views.hours_ahead),  #  第一种传参方式
    url(r'^xinlang/$',views.sina,{'offset':"ouguan"}),  #  第二种传参方式，字典形式

]

urlpatterns += [
    url(r'^app/',include("myapp.urls"))   #  起转接作用，跳转到相应app的urls文件


]
