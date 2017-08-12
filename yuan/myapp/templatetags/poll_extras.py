#coding=utf-8
'''
自定义过滤器，要在app里新建一个templatetags的文件夹，
这个目录应当和models.py 、views.py等处于统一层次
'''
from django import template

register = template.Library()

@register.filter(name = 'rep')
def rep(value,arg):
    return value.replace(arg,'#')
