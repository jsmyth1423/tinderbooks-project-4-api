from urllib import response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.request import Request
from .models import *
from .serializers.common import *
import random

# Create your views here.


class GameList(ListCreateAPIView):

    # Handles all games
    queryset = Game.objects.all()

    # Choose serializer to use
    serializer_class = PopulatedGameSerializer


class GameDetail(RetrieveAPIView):

    queryset = Game.objects.all()

    serializer_class = PopulatedGameSerializer


class GameRandom(ListCreateAPIView):
    queryset = Game.objects.all().order_by('?')[:1]
    serializer_class = PopulatedGameSerializer
