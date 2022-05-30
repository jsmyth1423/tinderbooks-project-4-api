from django.db import models

# Create your models here.


class Developer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=50)
    developer = models.ForeignKey(
        Developer, related_name='games', on_delete=models.CASCADE, null=True)
    image = models.CharField(max_length=200, blank=True)
    genres = models.ManyToManyField(Genre, related_name='games', blank=True)
    description = models.CharField(max_length=400, null=True)
    release_date = models.DateField(null=True)
    official_site = models.CharField(max_length=100, default=None, null=True, blank=True)

    def __str__(self):
        return self.name
