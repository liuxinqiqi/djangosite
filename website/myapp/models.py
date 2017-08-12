# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BookQuerySet(models.QuerySet):   #查找方法
    def little(self):
        return self.filter(id__lt = 4)


class  BookManager(models.Manager):
    def get_queryset(self):     #QuerySet是manager本身自带的对象，若定义新的queryset则需要重写进行覆盖
        return BookQuerySet(self.model,using = self._db)    #这一步是重写

    def title_count(self,keyword):
        return self.filter(title__icontains = keyword).count()

class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address =  models.CharField(max_length = 50)
    city =  models.CharField(max_length = 60)
    state_province =  models.CharField(max_length = 30)
    country =  models.CharField(max_length = 50)
    website =  models.URLField(verbose_name = '网址')     #verbose_name = ''修改website显示内容

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        ordering = ['address']
        verbose_name = "出版社"
        verbose_name_plural = verbose_name             #verbose_name_plural = " "  修改Publisher的显示名称

class  Author(models.Model):
    first_name =  models.CharField(max_length = 30)
    last_name =  models.CharField(max_length = 40)
    age = models.IntegerField(default = 10)
    email =  models.EmailField(blank = True)

    def __unicode__(self):
        return "%s  %s"%(self.first_name,self.last_name)

    class Meta:
        ordering = ['first_name']
        verbose_name_plural = "作者"

class Book(models.Model):
    title =  models.CharField(max_length = 100)
    publication_date = models.DateField(blank = True,null = True)
    # author_name = models.CharField(max_length = 60,null = True)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    objects = models.Manager()   #objects是models自动生成的，如果自定义，则要对views.py中的类的对象也进行修改
    myobjects = BookManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = "书目"

class Ad(models.Model):
    title = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = "avatar/%Y/%m",default = '1.png',verbose_name = "用户头像")

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = "广告"
