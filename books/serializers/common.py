from rest_framework import serializers
from ..models import *


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('__all__')


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('__all__')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('__all__')


class PopulatedBookSerializer(BookSerializer):
    author = AuthorSerializer()
    genres = GenreSerializer(many=True)


class BookWithGenresSerializer(BookSerializer):
    genres = GenreSerializer(many=True)


class PopulatedAuthorSerializer(AuthorSerializer):
    books = BookWithGenresSerializer(many=True)
