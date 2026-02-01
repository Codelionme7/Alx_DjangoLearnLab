from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from .models import Book
from .serializers import BookSerializer

# Existing BookList view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Updated BookViewSet with Permissions
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Step 3: secure this view
    permission_classes = [IsAuthenticated] 
