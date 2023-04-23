from django.db import models

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    question = models.TextField()
    url = models.URLField(max_length=255, blank=True)
    answer = models.URLField(max_length=255)
    tip = models.TextField()
    userAnswer = models.TextField(blank=True, null=True)