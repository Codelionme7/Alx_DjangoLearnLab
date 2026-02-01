from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Existing BookList view (Keep this)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New BookViewSet class
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
