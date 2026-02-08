from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
from rest_framework import filters

class BookListView(generics.ListAPIView):
    """
    View to list all books.
    - Allows filtering by title, author, and publication_year.
    - Allows searching by title and author.
    - Allows ordering by title and publication_year.
    - Publicly accessible (Read-Only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Task 2: Filtering, Searching, and Ordering
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year'] # Filtering
    search_fields = ['title', 'author__name'] # Searching
    ordering_fields = ['title', 'publication_year'] # Ordering

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by ID.
    - Publicly accessible (Read-Only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book.
    - Restricted to authenticated users only.
    - Performs validation via the serializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Custom logic can be added here (e.g., logging)
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.
    - Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Custom logic for updates can be placed here
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book.
    - Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
