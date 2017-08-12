# -*- coding: utf-8 -*-
import logging
import time
import datetime
from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from myapp.form import *
from django.conf import settings
from django.db.models import Count
from django.shortcuts import render, render_to_response,redirect, HttpResponse,HttpResponseRedirect
from django.db import connection
# from django.template import loader
from django.contrib import auth
from myapp.models import *
import json
from django.contrib.auth import logout, login, authenticate
from django.db.models import F,Q    #F整体操作，Q查找拼接条件
# from PIL import Image, ImageFilter
from django.core.paginator import Paginator,InvalidPage, EmptyPage, PageNotAnInteger
logger = logging.getLogger('myapp.views')
# Create your views here.



def global_setting(request):
    SITE_URL = "http://192.168.0.204:8000/"
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
    category_list = Category.objects.all()[:]  #分类
    archive_list = Article.objects.distinct_date()  #文章归档
    ad_list = Ad.objects.all()
    tag_list = Tag.objects.all()
    links_list = Links.objects.all()
    # #评论排行
    comment_count_list = Comment.objects.values('article').annotate(comment_count = Count('article')).order_by('-comment_count')   #评论排行
    comment_article_list = [Article.objects.get(pk = comment['article']) for comment in comment_count_list]
    #浏览量排行
    click_article_list = Article.objects.filter().order_by("-click_count")[:5]
    #站长推荐
    recommend_article_list = Article.objects.filter(is_recommend__gt =0).order_by("date_publish")[:5]
    return locals()

def getPage(request,a, n):       #分页
    # paginator = Paginator(a, n)
    # print type(paginator)
    # page = int(request.GET.get('page', 1))
    # print type(page)
    # a = paginator.page(page)
    # print type(a)
    # return a
    try:
        paginator = Paginator(a, n)
        page = int(request.GET.get('page', 1))
        a = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        a = paginator.page(1)
        print e
    return a


def index(request):
    try:
        ad_list = Ad.objects.all()
        tag_list = Tag.objects.all()
        links_list = Links.objects.all()
        # article_list = Article.objects.all()
        # # print type(article_list)
        # article_list = getPage(request, article_list, 2)
        # print type(article_list)
        print "aaaa"
    except Exception as e:
        print e
        logger.error(e)
    article_list = Article.objects.all()
    print type(article_list)
    article_list = getPage(request, article_list, 2)
    print type(article_list)
    return render(request, 'index.html',locals())



def category(request):
    try:
        cid = request.GET.get('cid',None)
        try:
            category = Category.objects.get(pk = cid)   #
        except Category.DoesNotExist:
            return render(request, 'failure.html',{'reason':"分类不存在"})
        article_list = Article.objects.filter(category = category)
        article_list = getPage(request, article_list, 2)
    except Exception as e:
        logger.error(e)
    return render(request, 'category.html', locals())

def archive(request):
    try:
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        article_list = Article.objects.filter(date_publish__icontains = year + '-' + month)
        article_list = getPage(request,article_list,2)
    except Exception as e:
        logger.error(e)
    return render(request, 'archive.html', locals())

def article(request):
    try:
        id = request.GET.get('id', None)
        try:
            article = Article.objects.get(pk = id)
            Article.objects.filter(id = id).update(click_count = F("click_count")+1)
        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason' : '没有找到对应文章'})
        #评论表单
        comment_form = CommentForm({'author' : request.user.username,
                                    'email' : request.user.email,
                                    # 'url' : request.user.url,
                                    # 'article' : id} if request.user.is_authenticated() else{'article' : id}
                                    })
        #获取评论信息
        # comments = Comment.objects.filter(article_id = id).order_by('id')
        # comment_list = []
        # for comment in comments:
        #     for item in comment_list:
        #         if not hasattr(item, 'children_comment'):
        #             setattr(item, 'children_comment', [])
            #     if comment.pid == item:
            #         item.children_comment.append(comment)
            #         break
            # if comment.pid is None:
            #     comment_list.append(comment)
        comment_list = Comment.objects.filter(article_id = id)
        print 'kljghjyftycutfot', comment_list
    except Exception as e:
        print e
        logger.error(e)
    comment_form = CommentForm()
    return render(request, 'article.html', locals())

# 提交评论
def comment_post(request):
    # print "zzzzzzzzzzz"
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        #获取表单信息
        # print "xxxxxxx"
        # print comment_form.cleaned_data['article']
        comment = Comment.objects.create(username = comment_form.cleaned_data["author"],
                                         email = comment_form.cleaned_data['email'],
                                        #  mobile = comment_form.cleaned_data['url'],
                                         content = comment_form.cleaned_data['comment'],
                                         article_id = 1,
                                         user = request.user if request.user.is_authenticated() else None)
        comment.save()
    else:
        print "ccccccccc"
        return render(request, 'failure.html', {'reason' : comment_form.errors})
    # try:
    #     comment_form = CommentForm(request.POST)
    #     if comment_form.is_valid():
    #         #获取表单信息
    #         print comment_form.cleaned_data['article']
    #         comment = Comment.objects.create(username = comment_form.cleaned_data["author"],
    #                                          email = comment_form.cleaned_data['email'],
    #                                         #  url = comment_form.cleaned_data['url'],
    #                                          content = comment_form.cleaned_data['comment'],
    #                                          article = comment_form.cleaned_data['article'],
    #                                          user = request.user if request.user.is_authenticated() else None)
    #         comment.save()
    #     else:
    #         return render(request, 'failure.html', {'reason' : comment_form.errors})
    # except Exception as e:
    #     logger.error(e)
    return redirect(request.META['HTTP_REFERER'])



# @permission_required('add_User',login_url = '/login')
# def thanks(request):
#     return HttpResponse('thanks for your register.')

# @login_required(login_url = '/thanks/')
# 注册
def reg(request):
    # try:
    #     print "------------"
    #     if request.method == 'POST':
    #         reg_form = RegForm(request.POST)
    #         print "========="
    #         if reg_form.is_valid():
    #             # 注册
    #             print "AAAAAAAAAA"
    #             user = User.objects.create(username=reg_form.cleaned_data["username"],
    #                                 email=reg_form.cleaned_data["email"],
    #                                 # url=reg_form.cleaned_data["url"],
    #                                 password=make_password(reg_form.cleaned_data["password"]),)
    #
    #             user.save()
    #
    #             # 登录
    #             # user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
    #             # login(request, user)
    #             print "777"
    #             return HttpResponseRedirect("/")
    #         else:
    #             return render(request, 'failure.html', {'reason': reg_form.errors})
    #     else:
    #         reg_form = RegForm()
    # except Exception as e:
    #     logger.error(e)
    print "------------"
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        print "========="
        if reg_form.is_valid():
            # 注册
            print "AAAAAAAAAA"
            user = User.objects.create(username=reg_form.cleaned_data["username"],
                                email=reg_form.cleaned_data["email"],
                                # url=reg_form.cleaned_data["url"],
                                password=make_password(reg_form.cleaned_data["password"]),)

            user.save()

            # 登录
            user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
            auth.login(request, user)
            print "777"
            return HttpResponseRedirect("/")
        else:
            return render(request, 'failure.html', {'reason': reg_form.errors})
    else:
        reg_form = RegForm()
    return render(request, 'reg.html', locals())

# @login_required(login_url = '/login/')
def login_test(request):
    return HttpResponse('thank you for login.')
#登录
def login(request):
    print "========"
    try:

        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            print "qqqqqqqqqq"
            if login_form.is_valid():
                print "aaaaaaaaaa"
                 #函数IsValid()    django form.is_valid() always returns false
                 #功能：检查对象变量是否已经实例化，即实例变量的值是否是个有效的对象句柄。
                 #语法：IsValid(objectname)
                 #参数：objectname:要检查的对象名。返回值：Boolean。
                 #如果指定对象已经创建了对此案实例，那么IsValid()函数返回True,否则返回FALSE。
                 #如果参数obejctname的值为NULL，IsValid()函数返回NULL。
                 # 检查对象变量是否已经实例化，即实例变量的值是否是个有效的对象句柄。
                #登录
                username = request.POST.get('username','')
                password = request.POST.get('password','')
                user = authenticate(username = username, password = password)
                if user is not None:
                    print "bbbbbbbbb"
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    auth.login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    print "nnnnnnnn"
                    return render(request, "failure.html", {'reason':'登录验证失败'})
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason' : login_form.errors})
        else:
            print "gggggggg"
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
    print "ssssssssss"
    return render(request, "login.html", locals())


def tag(request):
    name = request.GET.get('name', '')
    print name
    tag = Tag.objects.get(name = name)
    # article_list = Article.objects.filter(tag=tag)
    print tag
    article_list = tag.article_set.all()
    print article_list
    article_list = getPage(request, article_list,2)
    # try:
    #     # 先获取客户端提交的信息
    #     name = request.GET.get('name', None)
    #     print "aaa"
    #     try:
    #         tag = Tag.objects.get(name = name)
    #         print "bbb"
    #     except Category.DoesNotExist:
    #         return render(request, 'failure.html', {'reason': '分类不存在'})
    #     article_list = Article.objects.filter(tag=tag)
    #     article_list = getPage(request, article_list,2)
    # except Exception as e:
    #     logger.error(e)
    return render(request, 'tag.html', locals())


def logout(request):    #注销
    try:
        auth.logout(request)
        print '111'
    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'success.html', {'reason':'成功注銷'})
