# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 60, blank = True, null = True, verbose_name = '用户')
    password = models.CharField(max_length = 200, verbose_name = '密码')
    avatar = models.ImageField(upload_to = 'avatar/%Y/%m',\
    default = 'avatar/1.png',max_length = 200,blank = True,\
    null = True,verbose_name = '用户头像')
    qq = models.CharField(max_length = 20,blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length = 11,blank = True,null=True, verbose_name='个人网页地址')
    email = models.EmailField(max_length = 30, blank = True, null = True, verbose_name = '电子邮箱')

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        ordering = ['-id']

class Category(models.Model):
    name = models.CharField(max_length = 30, verbose_name = "分类名称")
    index = models.IntegerField(default = 999,verbose_name = "分类的排序")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "类型"
        verbose_name_plural = verbose_name
        ordering = ['index','id']



class ArticleManager(models.Manager):
    #自定义一个文章Model的管理器（1.新加一个数据处理的方法，2.改变原有的Queryset）
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%m Article')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


class Tag(models.Model):
    name = models.CharField(max_length = 30, verbose_name = "标签名称")
    # tag = models.ManyToManyField(Article)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name             #verbose_name_plural = " "  修改Publisher的显示名称


class Article(models.Model):

    title = models.CharField(max_length = 150, verbose_name = "文章标题")
    desc = models.CharField(max_length = 50,verbose_name = "文章描述")
    content = models.TextField(verbose_name = "文章内容")
    click_count = models.IntegerField(default = 0, verbose_name = "点击次数")
    is_recommend = models.BooleanField(default = False, verbose_name = "是否推荐")
    date_publish = models.DateTimeField(verbose_name = "发表时间")
    #增加外键 用户，类别，标签 以及增加 文章管理员类
    user = models.ForeignKey(User, verbose_name = "用户")
    category = models.ForeignKey(Category, blank = True, null = True, verbose_name = '分类')
    tag = models.ManyToManyField(Tag, verbose_name = "标签")
    objects = ArticleManager()
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name             #verbose_name_plural = " "  修改Publisher的显示名称
        ordering = ['-date_publish']

class Ad(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "广告标题")
    description = models.CharField(max_length = 100, verbose_name = "广告描述")
    image = models.ImageField(upload_to = 'ad/%Y/%m', verbose_name = "图片路径")
    date_publish = models.DateTimeField(auto_now_add = True, verbose_name = "发表时间")
    back_content = models.URLField(null = True,blank = True,verbose_name = "反馈内容")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "广告"
        verbose_name_plural = verbose_name
        ordering = ['id']



class Comment(models.Model):
    content = models.TextField(verbose_name = "评论内容")
    #null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空。
    #blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，
    #比如 admin 界面下增加 model 一条记录的时候。直观的看到就是该字段不是粗体
    username = models.CharField(max_length = 30,blank = True, null = True, verbose_name = '用户名')
    email = models.EmailField(max_length = 50,blank = True, null = True, verbose_name = "邮箱地址")
    url = models.URLField(max_length = 50, blank = True, null = True, verbose_name = "个人网页地址")
    date_publish = models.DateTimeField(auto_now_add = True, verbose_name = "发表时间")
    #增加外键 用户，文章，父级评论
    user = models.ForeignKey(User, blank = True, null = True, verbose_name = "用户")
    article = models.ForeignKey(Article,blank = True, null = True, verbose_name = "文章")
    #父级评论
    parent_id = models.ForeignKey('self', blank = True, null = True, verbose_name = "父级评论")

    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name             #verbose_name_plural = " "  修改Publisher的显示名称



class Links(models.Model):
    title = models.CharField(max_length = 30, verbose_name = "标题")
    back_content = models.URLField(verbose_name = '返回网页')
    desc = models.CharField(max_length = 100, verbose_name = "链接描述")
    date_publish = models.DateTimeField(auto_now_add = True, verbose_name = "发布时间")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name
        ordering = ['id']
