from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]
admin.site.register(Article, ArticleAdmin)