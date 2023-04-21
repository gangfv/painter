from django.contrib import admin
from django.contrib.auth.models import Group

from home.models import Lesson, Form

admin.site.unregister(Group)
admin.site.register(Lesson)
admin.site.register(Form)
