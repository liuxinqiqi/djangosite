# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myapp.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Ad)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Links)
