from django.db.models import CASCADE
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=CASCADE, related_name='books')
    category = models.ManyToManyField(Category, related_name='books')
    rating = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.title} - {self.description}'
