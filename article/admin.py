from django.contrib import admin
from .models import Article, ArticleCategory

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields]

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArticleCategory._meta.fields]

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
