from django.urls import path
from .views import *

urlpatterns = [
    # Generic views for books
    path('books/', BookList.as_view()),
    path('books/detail/<int:pk>/', BookDetail.as_view()),

]
