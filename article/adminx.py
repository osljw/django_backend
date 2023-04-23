import xadmin

from .models import Article


class ArticleAdmin:
    list_display = ["id", "auth", "tags", "title", "body", "is_show"]
xadmin.site.register(Article, ArticleAdmin)

# class ArticleCategoryAdmin:
#     list_display = ["title"]
# xadmin.site.register(ArticleCategory, ArticleCategoryAdmin)