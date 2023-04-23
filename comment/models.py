from django.db import models

from user_auth.models import User
from article.models import Article
# Create your models here.


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='评论作者'
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.DO_NOTHING,
        verbose_name='评论文章'
    )

    content = models.TextField(verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        db_table = "comment_info"
        verbose_name = "评论信息"

    def __str__(self) -> str:
        return self.content