from django.contrib import admin
from .models import *


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


class FuncAdmin(admin.ModelAdmin):
    list_display = ['func', 'description', 'language', 'id']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'size', 'range']


admin.site.register(Tag, TagAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Func, FuncAdmin)
admin.site.register(Type, TypeAdmin)
