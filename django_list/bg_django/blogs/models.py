from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id = models.IntegerField(default=0)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    title = models.CharField(max_length=60,default='')
    desc = models.CharField(max_length=250,default='')

