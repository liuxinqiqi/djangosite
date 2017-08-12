# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from myapp.models import *

# Register your models here.



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name','email')


class BookAdmin(admin.ModelAdmin):
    list_filter = ('publication_date',)  #元组，只有一项时要加逗号
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)   #若排序冲突，以此为准
    field = ('title','Author','publisher','publication_date')


admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Ad)
