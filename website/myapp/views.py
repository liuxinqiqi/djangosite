# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response   #render
from django.http import HttpResponse,Http404
from django.template import loader
import time
from myapp.models import *
from django.db.models import F,Q    #F整体操作，Q查找拼接条件
import datetime
from django.core.paginator import Paginator,InvalidPage,PageNotAnInteger
from PIL import Image, ImageFilter

# Create your views here.
def global_setting(request):
    NAME = 'cainiao'
    TEL = '18810207835'
    MOTTO = '业精于勤荒于嬉,行成于思毁于随。'
    return locals()

def fun():
    return 'www'

class A(object):
    a = "A ==> a"
    def f(self):
        return "just A ==> f"


def first(request):
    return HttpResponse("it is my first app")

def bs(request):
    t = loader.get_template('bs.html')
    html = t.render({})  #render：模板对象的一个属性
    return HttpResponse(html)

def test(request):
    # return render_to_response('bs.html',{})
    return render(request,'bs.html',{})  #render:和上一个不同，是由django文件中直接导入的一个功能

def temp(request):
    datetime = time.localtime()
    # return render(request,'time.htmls',{'datetime':t})
    return render(request,'time.html',locals())

def display_meta(request):
    num = 1
    s = "hello"
    l = [1,2,5,'e','listtttt']
    t = (4,6,7,'tupleeeee')
    d = {'a':'one','b':'two','c':'three'}
    f = fun()
    obj = A()

    return render(request,'meta.html',{'nummm':num,'ss':s,'list':l,'tuple':t,'dict':d,'fun':f,'objjj':obj})

def tag(request):
    error = "error"
    l = [1,2,3,4]
    # return render(request,'tags.html',{error:'a','list':l})
    return render(request,'tags.html')

def filter_f(request):
    num = 1
    s = "HELLO WORLD!"
    return render(request,'filter.html',{'num':num,'s':s})

def base(request):
    return render(request,'extend.html',{})

def nav(request):
    return render(request,'nav.html',{})

def load(request):
    return render(request,'static.html',{})
def mydb(request):
    pass
    # 增1    create() 直接创建数据记录
    # Author.objects.create(first_name = 'Jame',last_name = 'Green',email = 'jm@123.com')
    # Author.objects.create(first_name = 'Jone',last_name = 'Smith',email = 'js@123.com')
    # Author.objects.create(first_name = 'Meimei',last_name = 'Han',email = 'hm@123.com')
    # Author.objects.create(first_name = 'Lei',last_name = 'Li',email = 'll@123.com')
    # Author.objects.create(first_name = 'Lili',last_name = 'Cai',email = 'cl@123.com')

    # Publisher.objects.create(name = '人民出版社',address= '北京',city = '海淀',state_province = 'beijing',country = 'China',website = 'http://baidu')
    # Publisher.objects.create(name = '高等教育出版社',address = '陕西',city = '西安',state_province = 'xian',country = 'China',website = 'http://taobao')
    # Publisher.objects.create(name = '同济大学出版社',address = '上海',city = '浦东',state_province = 'shanghai',country = 'China',website = 'http://wangyi')
    #
    # Book.objects.create(title = "python",publication_date = datetime.datetime.now(),publisher_id = 1)
    # Book.objects.create(title = "math",publication_date = datetime.datetime.now(),publisher_id = 2)
    # Book.objects.create(title = "html5",publication_date = datetime.datetime.now(),publisher_id = 3)
    # Book.objects.create(title = "java",publication_date = datetime.datetime.now(),publisher_id = 4)

    #增2
    # dic = {'first_name' : 'Jame','last_name' : 'Green','email' : 'jm@123.com'}
    # obj = Author(**dic)
    # obj.save()     #模块对象调用，用于同步数据库

    #删除   delete() 删除记录
    # Author.objects.filter(id__gt = 5).delete()
    #
    # #改1  update() 更新记录
    # Author.objects.filter(id = 3).update(first_name = 'lili')
    # #改2
    # obj = Author.objects.get(id = 2)
    # obj.first_name = "lucy"
    # obj.save()

    #查  select * from author     all() 取出所有记录 --->values/values_list/count()/order_by()
    # a = Author.objects.all()   #取出每一条记录生成一个对象
    # b = Author.objects.all().values('email')    #生成所有记录的指定字段
    #取出所有记录的指定字段
    # c = Author.objects.all().values_list('first_name','email')
    #获取某一记录的对象   get() 得到一个对象 不能取范围或者不存在的值
    # d = Author.objects.get(id = 1).first_name
    # d = Author.objects.get(id = 1)
    # d.first_name
    # 使用过滤器获取某一记录的对象  filter() 得到一个对象列表 无法像get一样直接调用.first_name
    # e = Author.objects.filter(id = 1)[0].email
    # e = Author.objects.filter(id = 1)
    # e[0].email

    # f = Author.objects.exclude(id = 1)[3].first_name

    # q = Q()
    # print dir(q)
    # q.connector = 'AND'
    # q.children.append(('id',3))
    # q.children.append(('last_name','Green'))
    #
    # g = Author.objects.filter(q)
    #
    # Book.objects.filter().update(age = F('age') +1)
    #
    # return HttpResponse('g[0].first_name')
    return HttpResponse("ok")

def mtm(request):    #用 models1 进行调用

    book1 = Book.objects.get(id = 9)  #获取 id 为 2 的 book 并赋值给book1
    s = book1.publisher.name    # 通过book获取Publisher和Author不加_set,获取book1的出版社名字
    # return HttpResponse(s)

    pub1 = Publisher.objects.get(id = 1)   #用 多 查找 一 时，直接些，但publisher要小写   获取id为1的出版社，并赋值给pub1
    book_list = pub1.book_set.all()   #用 book搜索Author和Publisher时，book小写，后加_set，用all进行查找    获取pub1出版的书，并列出


    author1 = Author.objects.get(id = 1)    #获得id 为1 的作者信息，并赋值给author1
    book1_list = author1.book_set.all()    #查找book要用_set     获得author1 所有的书，并生成列表

    author_list = book1.author.all()       #获得 book1 的所有作者

    # count = Book.myobjects.title_count('java')
    # return HttpResponse(count)

    book2_list = Book.myobjects.all().little()    #all()调用的就是QuerySet()
    return HttpResponse(book2_list)
    # return HttpResponse(author_list[1].first_name)
    # return HttpResponse(book1_list[1].title)


def page(request,article_list,n):
    paginator = Paginator(article_list,n)        #paginator是分页器
    try:
        p = int(request.GET.get('page',1))   #get取page，若没有，则取第二个参数1
        article_list = paginator.page(p)
    except (EmptyPage,InvalidPage,PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list
def getpage(request):
    article_list = ['a1','a2','a3','a4','a5','a6','a7']
    article_list = page(request,article_list,5)
    return render(request,'page.html',{'article_list':article_list})


def postImage(request):
    return render(request,'image.html',{})


def message(request):
    try:
        # img = Ad(title = "imgtest", img = request.FILES.get('picfile'))
        img = Ad(title = "imgtest", img = request.GET.get('picfile'))
        img.save()
    except Exception,e:
        return HttpResponse("Error:%s"%e)
    return HttpResponse("postImage")


# def message(request):
#     try:
#         imgFile = request.FILES['picfile']
#         img = Image.open(imgFile)
#         img.save("/home/linux/djangosite/website/media/1.png",'png')
#     except Exception,e:
#         return HttpResponse("Error:%s"%e)
#     return HttpResponse("post images")
