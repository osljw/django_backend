from django.contrib import admin
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Page._meta.fields]
admin.site.register(Page, PageAdmin)
