from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True, null=True)
