import os
import glob
from pathlib import Path


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_backend.settings")
import django
django.setup()

from article.models import Article, ArticleCategory
from user_auth.models import User


# articles = Article.objects.filter(id__gt = 5)
# print(articles)
# articles.delete()

# cats = ArticleCategory.objects.filter(id__gt = 1)
# print(cats)
# cats.delete()