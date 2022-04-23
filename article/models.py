from unicodedata import category
from django.db import models
from django.db.models import (
    CharField,
    DateTimeField,
    TextField,
    BooleanField,
)

from user_auth.models import User

# Create your models here.

class ArticleCategory(models.Model):
    title = CharField(max_length=100, verbose_name="文章类别")
    create_time = DateTimeField(auto_now_add=True, verbose_name="类别创建时间")

    class Meta:
        db_table = "article_category"
        verbose_name = "文章分类"
    
    def __str__(self) -> str:
        return self.title

class Article(models.Model):
    # User:Article = 1:n
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    # ArticleCategory:Article = 1:n
    category = models.ForeignKey(ArticleCategory, blank=True, on_delete=models.CASCADE)

    title = CharField(max_length=255, verbose_name="article title")
    
    create_time = DateTimeField(auto_now_add=True, verbose_name="article create_time")
    update_time = DateTimeField(auto_now=True, verbose_name="article update_time")
    body = TextField()
    is_show = BooleanField(default=True, verbose_name="article show status")

    class Meta:
        db_table = "article_detail"
        verbose_name = "文章详情"

    def __str__(self) -> str:
        return self.title


