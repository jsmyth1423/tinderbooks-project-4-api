from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import *
from .serializers.common import *


# Create your views here.


class GameList(ListCreateAPIView):

    # Handles all games
    queryset = Game.objects.all()

    # Choose serializer to use
    serializer_class = PopulatedGameSerializer


class GameDetail(RetrieveAPIView):

    queryset = Game.objects.all()

    serializer_class = PopulatedGameSerializer
