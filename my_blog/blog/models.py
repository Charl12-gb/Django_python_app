from distutils.command.upload import upload
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title