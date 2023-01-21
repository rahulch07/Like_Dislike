from django.db import models

# Create your models here.
class Like(models.Model):
    #likes = models.ManyToManyField(User, related_name='post')
    likes = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)