from django.db import models

# Create your models here.


class Comment(models.Model):
    comments = models.CharField(max_length=1500)
    likes = models.PositiveIntegerField(default=0, blank=True, null=True)
    dislikes = models.PositiveIntegerField(default=0, blank=True, null=True)
    replies = models.CharField(max_length=1500, blank=True, null=True)
    video = models.CharField(max_length=150, blank=True, null=True)
    
    