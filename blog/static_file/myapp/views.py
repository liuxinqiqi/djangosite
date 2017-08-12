# -*- coding: utf-8 -*-
import logging
import time
import datetime
from django.contrib.auth.hashers import make_password
from myapp.form import *
from django.conf import settings
from django.db.models import Count
from django.shortcuts import render, render_to_response,redirect, HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required,permission_required
from myapp.models import *
import datetime
from django.db.models import F,Q    #F整体操作，Q查找拼接条件
from PIL import Image, ImageFilter
from django.core.paginator import Paginator,InvalidPage,PageNotAnInteger
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
    # comment_count_list = Comment.objects.values('article').\
    # annotate(comment_count = Count('article')).order_by('-comment_count')   #评论排行
    # article_comment_list = [Article.objects.get(pk = comment['article']) for comment in comment_count_list]
    #浏览量排行
    #站长推荐
    return locals()

def getPage(request,article_list):       #分页
    paginator = Paginator(article_list, 3)
    try:
        page = int(request.GET.get('page',1))
        article_list = paginator.page(page)
    except (Emptypage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list

def index(request):
    try:
        ad_list = Ad.objects.all()
        tag_list = Tag.objects.all()
        links_list = Links.objects.all()
        article_list = Article.objects.all()
        article_list = getPage(request, article_list)
    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'index.html',locals())



def category(request):
    try:
        cid = request.GET.get('cid',None)
        try:
            category = Category.objects.get(pk = cid)   #
        except Category.DoesNotExist:
            return render(request, 'failure.html',{'reason':"分类不存在"})
        article_list = Article.objects.filter(category = category)
        article_list = getPage(request, article_list)
    except Exception as e:
        logger.error(e)
    return render(request, 'category.html', locals())

def archive(request):
    try:
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        article_list = Article.objects.filter(date_publish__icontains = year + '-' + month)
        article_list = getPage(request,article_list)
    except Exception as e:
        logger.error(e)
    return render(request, 'archive.html', locals())

def article(request):
    try:
        id = request.GET.get('id', None)
        try:
            article = Article.objects.get(pk = id)
        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason' : '没有找到对应文章'})
        #评论表单
        comment_form = CommentForm({'author' : request.user.username,
                                    'email' : request.user.email,
                                    'url' : request.user.url,
                                    'article' : id} if request.user.is_authenticated() else{'article' : id})
        #获取评论信息
        comments = Comment.objects.filter(article = article).order_by('id')
        comment_list = []
        for comment in comments:
            for item in comment_list:
                if not hasattr(item, 'children_comment'):
                    setattr(item, 'children_comment', [])
                if comment.pid == item:
                    item.children_comment.append(comment)
                    break
            if comment.pid is None:
                comment_list.append(comment)
    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'article.html', locals())

# 提交评论
def comment_post(request):
    try:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            #获取表单信息
            comment = Comment.objects.create(username = comment_form.cleaned_data["author"],
                                             email = comment_form.cleaned_data['email'],
                                             url = comment_form.cleaned_data['url'],
                                             content = comment_form.cleaned_data['comment'],
                                             article_id = comment_form.cleaned_data['article'],
                                             user = request.user if request.user.is_authenticated()else None)
            comment.save()
        else:
            return render(request, 'failure.html', {'reason' : comment_form.errors})
    except Exception as e:
        logger.error(e)
    return redirect(request.META['HTTP_REFERER'])



@permission_required('add_User',login_url = '/login')
def thanks(request):
    return HttpResponse('thanks for your register.')

# @login_required(login_url = '/thanks/')
def reg(request):
    print "=============="
    # try:
    #     if request.method == 'POST':
    #         print "aaaaaaaaaaaaaaaaa"
    #         reg_form = RegForm(request.POST)
    #         if reg_form.is_valid():
    #             cd = reg_form.cleaned_data
    #             #注册
    #             user = User.objects.create(username = cd['username'],\
    #             password = make_password(cd['password']),\
    #             email = cd['email'])
    #             user.save()
    #             #登录
    #             user.backend = 'django.contrib.auth.backends.ModelBackend'
    #             login(request, user)
    #             return redirect(request.POST.get('source_url'))
    #         else:
    #             return render(request,'failure.html',{'reson':reg_form.errors})
    #     else:
    #         print "bbbbbbbbbbbbbbbbbbb"
    #         reg_form = RegForm()
    # except Exception as e:

    if request.method == 'POST':
        print "aaaaaaaaaaaaaaaaa"
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            cd = reg_form.cleaned_data
            #注册
            user = User.objects.create(username = cd['username'], password = make_password(cd['password']), email = cd['email'])
            user.save()
            #登录
            # user.backend = 'django.contrib.auth.backends.ModelBackend'
            # login(request.user)
            return HttpResponseRedirect(request.POST.get('source_url'))
        else:
            return render(request,'failure.html',{'reson':reg_form.errors})
    else:
        print "bbbbbbbbbbbbbbbbbbb"
    reg_form = RegForm()
    # logger.error(e)
    return render(request,'reg.html',{'reg_form':reg_form})

# @login_required(login_url = '/login/')
def login_test(request):
    return HttpResponse('thank you for login.')
#登录
def login(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
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
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                else:
                    return render(request, "failure.html", {'reason':'登录验证失败'})
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason' : login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
        return render(request, "login.html", locals())


def tag(request):
    try:
        name = request.GET.get('tag', '')
        tag = Tag.objects.get(name = name)
        article_list = tag.article_set.all()
        article_list1 = []
        for article in article_list:
            n = article.id
            comment_count = Comment.objects.filter(art_id = n).count()
            article.comment_count = comment_count
            article_list1.append(article)
        article_list = page(request, article_list1, 3)
    except Exception as e:
        return render(request, 'failure.html', {'errors' : "没有此标签的文章"})
    return render(request, 'tag.html', {'article_list': article_list, 'name' : name})


def logout(request):    #注销
    try:
        logout(request)
    except Exception as e:
        print e
        logger.error(e)
    return redirect(request.META['HTTP_REFERER'])
