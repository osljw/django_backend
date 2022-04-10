from django.db import models
from django.db.models import (
    BooleanField, 
    CharField,
    IntegerField,
    ImageField,
)

# Create your models here.


class Banner(models.Model):
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