from django.db import models

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    question = models.TextField()
    options = models.TextField(blank=True)
    url = models.URLField(max_length=255, blank=True)
    answer = models.TextField()
    tip = models.TextField(blank=True)
    userAnswer = models.TextField(blank=True, null=True)