from django.db import models

# Create your models here.

class Author(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Genre(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name


class Book(models.Model):
  title = models.CharField(max_length=50)
  author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE, null=True)
  image = models.CharField(max_length=200, blank=True)
  genres = models.ManyToManyField(Genre, related_name='book', blank=True)
  release_date = models.DateField(null=True)

  def __str__(self):
    return self.title