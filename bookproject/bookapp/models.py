from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    language = models.CharField(max_length=250)
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
