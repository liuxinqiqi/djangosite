# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from formapp.forms import RemarkForm,AuthorForm,BookForm
# from formapp.forms import *
from myapp.models import Book,Author

# Create your views here.
def search_form(request):
    return render(request,'search_form.html',{})

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        return HttpResponse("I have get a '%s'"%q)
    else:
        return render(request,'search.html',{'error':True})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject')

        if not request.POST.get('email',''):
            errors.append('Enter a email address')

        if not request.POST.get('message',''):

            errors.append('Enter a message')

        if not errors:
            return HttpResponseRedirect('/form/contact/thanks')

    return render(request,"contact_form.html",{"errors":errors,'subject':request.POST.get('subject'),'email':request.POST.get('email'),'message':request.POST.get('message')})


def thanks(request):
    print "come on"
    # return HttpResponse("Thanks,we have get your message.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def formtest(request):
    form = RemarkForm()
    # print form
    # for i in form:
    #     print i
    #     print "=============================="
    # print dir(form)

    if request.method == 'POST':   #判断是否与formset.html中的method一致
        form = RemarkForm(request.POST)
        if form.is_valid():    #判断是否合法
            cd = form.cleaned_data    #清空表单数据
            print cd['subject']     #后台打印
            print cd['mail']
            print cd['topic']
            print cd['message']
            print cd['cc_myself']
            return HttpResponseRedirect('/form/form')    #重新刷新页面
    else:
        form = RemarkForm()
        # print dir(form)
    return render(request,'formset.html',{'form':form})
    #return中的form，a，b都是用来将 键 所指向的 值 传递 到formset.html中，并在网页页面中显示



def bookset(request):
    if request.method == 'POST':
        # form = BookForm(request.POST)
        form = AuthorForm(request.POST)
        if form.is_valid():    #判断是否合法
            cd = form.cleaned_data    #清空表单数据
            dic = {'first_name':cd['first_name'],'last_name':cd['last_name'],'age':cd['age'],'email':cd['email']}
            # dic = {'id': 25,'title':cd['title'],'author_id':cd['author'],'publisher_id':9,'publisher':cd['publisher']}
            # dic = {'title':cd['title'],'publication_date': '2017-07-21','publisher_id':9}
            Author.objects.create(**dic)
            return HttpResponseRedirect('/form/bookform')    #重新刷新页面
    else:
        # form = RemarkForm()
        form = AuthorForm()
        # print dir(form)
    return render(request,'bookset.html',{'form':form})
    # return render(request,'bookset.html',{'form':form,'a':"sfgdtey",'b':"sdfser"})
    #return中的form，a，b都是用来将 键 所指向的 值 传递 到formset.html中，并在网页页面中显示
