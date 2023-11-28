from django.db import models
from django.db.models import (
    IntegerField,
    CharField,
    DateTimeField,
    URLField,
    TextField,
    BooleanField,
)
# Create your models here.


class Page(models.Model):
    FORMAT_CHOICES = [
        ('mdx', 'MDX'),
        ('html', 'Html'),
    ]
    
    url = CharField(max_length=255, verbose_name="page url")
    type = models.CharField(max_length=10, choices=FORMAT_CHOICES, default="mdx")
    body = TextField()
    valid = BooleanField(default=True, verbose_name="page status")

    def __str__(self):
        return self.url
    
    class Meta:
        db_table = "page_detail"
        verbose_name = "页面详情"