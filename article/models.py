from unicodedata import category
from django.db import models
from django.db.models import (
    IntegerField,
    CharField,
    DateTimeField,
    TextField,
    BooleanField,
    
)
from taggit.managers import TaggableManager

from user_auth.models import User

# Create your models here.

# class ArticleCategory(models.Model):
#     category = CharField(max_length=100, unique=True, primary_key=True, verbose_name="文章类别")
#     parent_category = CharField(max_length=100, verbose_name="父目录")
#     level = IntegerField(default=1, verbose_name="目录级别")
#     create_time = DateTimeField(auto_now_add=True, verbose_name="类别创建时间")
    
#     class Meta:
#         db_table = "article_category"
#         verbose_name = "文章分类"
    
#     def __str__(self) -> str:
#         return f"title:{self.title}, parent: {self.parent_title}, level: {self.level}, path: {self.path}"

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="栏目名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="栏目创建时间")
    class Meta:
        db_table = "article_category"
        verbose_name = "文章栏目"
    def __str__(self):
        return self.name
    
class Article(models.Model):
    # User:Article = 1:n
    auth = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # ArticleCategory:Article = m:n
    categories = models.ManyToManyField(ArticleCategory, blank=True, related_name='articles')
    
    tags = TaggableManager(blank=True)

    title = CharField(max_length=255, verbose_name="article title")
    body = TextField()
    
    create_time = DateTimeField(auto_now_add=True, verbose_name="article create_time")
    update_time = DateTimeField(auto_now=True, verbose_name="article update_time")
    
    is_show = BooleanField(default=True, verbose_name="article show status")

    class Meta:
        db_table = "article_detail"
        unique_together = (("auth", "title"),)
        verbose_name = "文章详情"

    def __str__(self) -> str:
        return self.title


