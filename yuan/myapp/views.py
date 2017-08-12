# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

from django.http import HttpResponse,Http404
from django.template import loader # 导入加载器头文件
import time
# Create your views here.
def fun():
    return "teacher"
    # return a

class A(object):
    a = "hello world"
    def f(self):
        return "This is a A:fun "

def hello (request):
    return HttpResponse("hello world")

def first(request):
    return HttpResponse("my first app")

def bs(request):   #  模板
    t = loader.get_template('bs.html')
    html = t.render({})    #  传参处理
    return HttpResponse(html)

def test(request):     # test 函数与 bs函数实现的 功能一样
    # return render_to_response('bs.html',{})  # render_to_response 比较老
    return render(request,'bs.html',{})  # 全局传参

def temp(request):
    #  第一种传参方式，单个变量
    # t = time.localtime()
    # return render(request,'time.html',{'datetime':t})

    # 第二种传参方法，多个变量使用
    datetime = time.localtime()  #  定义的变量名时，要与模板中的变量名一致
    return render(request,'time.html',locals())  # locals 收集局部的变量形成字典的键值形式

def display_meta(request):
    num = 1
    s = "hello"
    l = [1,2,'c','nihao']
    t = (4,5,'d','tuple')
    d = {'a':'one','b':'two','c':'three'}
    f = fun()
    obj = A()
    return render(request,'meta.html',\
    {'num':num,'s':s,'list':l,'tuple':t,'dict':d,'fun':f,'obj':obj})

#  标签
def tag(request):
    error = "error"
    l = [1,2,3,4,5,6,7]
    return render(request,'tags.html',{'error':error,'list':l})
# 过滤器
def fil(request):
    num = 1
    s = "HELLO  WORLD"
    return render(request,'filter.html',{'num':num,'s':s})

def base(request):
    return render(request,'extend.html',{})

def nav(request):
    return render(request,'nav.html',{})

#  模板的全局变量，要在setting的 TEMPLATES 中定义
def global_setting(request):
    NAME = "cainiao"
    TEL = '18810207835'
    GEYAN = '业精于勤而荒于嬉，行成于思而毁于随'

    return locals()

# 静态文件加载
def load(request):
    return render(request,'static.html',{})
'''
静态文件的加载，要在settings 中写
STATICFILES_DIRS = (
    BASE_DIR,'static'
)
'''
