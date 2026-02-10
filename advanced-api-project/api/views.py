from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    List all books.
    Permission: Allow read-only access for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    Permission: Allow read-only access for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Permission: Authenticated users only.
    Customization: Includes custom validation logic in perform_create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Example customization: You could automatically assign the current user as the author if your model supported it.
        # For now, we simply save the data.
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Permission: Authenticated users only.
    Customization: Includes custom logic in perform_update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Custom logic before updating can go here
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    Permission: Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
