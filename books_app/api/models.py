from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=30)
    year = models.IntegerField()
    language = models.CharField(max_length=10)
    original_language = models.CharField(max_length=10)
    genres = models.CharField(max_length=30)
    page_nr = models.IntegerField()
    ISBN = models.CharField(max_length=20)
