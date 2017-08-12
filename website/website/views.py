#coding=utf-8

from django.http import HttpResponse,Http404
from django.template import loader
import datetime


def home(request):
    return HttpResponse("<h1>my first html<h1>")

def index(request):
    return HttpResponse("<h1>hello world!<h1>")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>it is now %s.<body><html>"%now
    return HttpResponse(html)

# def bs(resquest):
#     t = loader.get_template('bs.html')
#     html = t.render({'time':datetime.datetime.now()})   #传递后台参数
#     return HttpResponse(html)

def hours_ahead(resquest,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hours,it will be %s.<body><html>"%(offset,dt)
    return HttpResponse(html)

def sina(request,offset):
    if offset == "yingchao":
        return HttpResponse("英超界面")
    elif offset == "ouguan":
        return HttpResponse("欧冠界面")
    else:
        raise Http404()
