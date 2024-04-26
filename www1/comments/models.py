from django.db import models

class Comment(models.Model):
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    creation_date = models.DateField(default=None)
    published_from = models.DateField(default=None)
