from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields]
admin.site.register(Article, ArticleAdmin)

