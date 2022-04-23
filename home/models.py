from tabnanny import verbose
from django.db import models
from django.db.models import (
    BooleanField, 
    CharField,
    IntegerField,
    ImageField,
    DateTimeField,
)

# Create your models here.

class BaseModel:
    create_time = DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = DateTimeField(auto_now=True, verbose_name="修改时间")

class Banner(BaseModel, models.Model):
    img_url = ImageField(upload_to="banner", max_length=255, verbose_name="img url")
    link_url = CharField(max_length=500, verbose_name="link url")
    is_show = BooleanField(default=True, verbose_name="should img show")
    orders = IntegerField(default=1, verbose_name="img show order")
    title = CharField(max_length=500, verbose_name="ad title")

    class Meta:
        db_table = "banner"
        verbose_name = "banner img"

    def __str__(self) -> str:
        return self.title

class NarBar(BaseModel, models.Model):
    POSITION_CHOICES = (
        (1, "top nav"),
        (2, "bottom nav"),
    )
    title = CharField(max_length=255, verbose_name="nav title")
    orders = IntegerField(default=1, verbose_name="nav order")
    link_url = CharField(max_length=500, verbose_name="nav url")
    is_show = BooleanField(default=True, verbose_name="nav show status")
    position = IntegerField(choices=POSITION_CHOICES, verbose_name="nav position")
    is_insite = BooleanField(default=True, verbose_name="是否为站内导航")
    
    class Meta:
        db_table = "navbar"
        verbose_name = "导航栏"

    def __str__(self) -> str:
        return self.title