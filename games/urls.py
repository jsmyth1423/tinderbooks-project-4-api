from django.urls import path
from .views import *

urlpatterns = [
    # Generic views for games
    path('games/', GameList.as_view()),
    path('games/detail/<int:pk>/', GameDetail.as_view()),
    path('games/random', GameRandom.as_view())
]
