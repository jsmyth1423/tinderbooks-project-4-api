from rest_framework import serializers

from jwt_auth.serializers import UserSerializer
from ..models import *


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('__all__')


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = ('__all__')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('__all__')


class PopulatedGameSerializer(GameSerializer):
    developer = DeveloperSerializer()
    genres = GenreSerializer(many=True)
    SwipedBy = UserSerializer(many=True)


class GameWithGenresSerializer(GameSerializer):
    genres = GenreSerializer(many=True)


class PopulatedDeveloperSerializer(DeveloperSerializer):
    games = GameWithGenresSerializer(many=True)
