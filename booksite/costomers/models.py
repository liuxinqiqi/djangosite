# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    title =  models.CharField(max_length = 100)
    publication_date = models.DateField(blank = True,null = True)
    def __unicode__(self):      #
        return self.title

    class Meta:
        ordering = ['title']



class Aa():
    def __init__(self,title):
        self.title = title

    def __unicode__(self):    #用于显示类的对象在网页中的显示名称，若有__unicode__()函数，则显示名称，否则显示"类+object"
    #一个类如果定义了__unicode__方法, 那么你
    #可以使用这个类的对象构造一个unicode对象, 调用unicode(obj)就构造完成了,
    #unicode是一个类, 这就是调用一下构造函数.
        return self.title

a = Aa('title')
print a
