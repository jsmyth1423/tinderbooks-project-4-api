from django.db import models
from django.contrib.auth.models import AbstractUser
from games.models import Game

# Create your models here.


class CustomUser(AbstractUser):
    swipedGames = models.ManyToManyField(Game, related_name='SwipedBy', default=None, blank=True)
