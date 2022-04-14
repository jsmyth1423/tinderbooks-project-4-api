from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import *
from .serializers.common import *


# Create your views here.


class BookList(ListCreateAPIView):

    # Handles all books
    queryset = Book.objects.all()

    # Choose serializer to use
    serializer_class = PopulatedBookSerializer


class BookDetail(RetrieveAPIView):

    queryset = Book.objects.all()

    serializer_class = PopulatedBookSerializer
