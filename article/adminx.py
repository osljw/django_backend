import xadmin
from xadmin import views
from .models import Article, ArticleCategory


class ArticleAdmin:
    list_display = ["auth", "category", "title", "body", "is_show"]

xadmin.site.register(Article, ArticleAdmin)

class ArticleCategoryAdmin:
    list_display = ["title"]

xadmin.site.register(ArticleCategory, ArticleCategoryAdmin)