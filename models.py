from django.db import models
# Create your models here.

class Blogpost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    
    class Meta:
        verbose_name_plural='我的博客'

    def __str__(self):
        return self.title
