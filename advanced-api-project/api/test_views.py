from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author
from django.urls import reverse

class BookAPITests(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, permissions, filtering, searching, and ordering.
    """

    def setUp(self):
        """
        Set up the test environment.
        Creates a test user, an author, and a book before each test runs.
        """
        # Create a user for authentication testing
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create an Author
        self.author = Author.objects.create(name="J.K. Rowling")
        
        # Create a Book
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        
        # Define URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    # --- CRUD Tests ---

    def test_create_book_authenticated(self):
        """Test that an authenticated user can create a book."""
        self.client.login(username='testuser', password='password')
        data = {
            'title': 'Chamber of Secrets',
            'publication_year': 1998,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(response.data['title'], 'Chamber of Secrets')

    def test_create_book_unauthenticated(self):
        """Test that an unauthenticated user cannot create a book."""
        data = {
            'title': 'Prisoner of Azkaban',
            'publication_year': 1999,
            'author': self.author.id
        }
        # No login performed
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book(self):
        """Test updating a book."""
        self.client.login(username='testuser', password='password')
        data = {
            'title': 'Updated Title',
            'publication_year': 1997,
            'author': self.author.id
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.login(username='testuser', password='password')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # --- Filtering, Searching, Ordering Tests ---

    def test_filter_by_title(self):
        """Test filtering books by title."""
        # Create another book to ensure filter works
        Book.objects.create(title="Another Book", publication_year=2000, author=self.author)
        
        response = self.client.get(self.list_url, {'title': "Harry Potter and the Philosopher's Stone"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter and the Philosopher's Stone")

    def test_search_functionality(self):
        """Test searching for books."""
        Book.objects.create(title="Fantastic Beasts", publication_year=2001, author=self.author)
        
        response = self.client.get(self.list_url, {'search': 'Harry'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter and the Philosopher's Stone")

    def test_ordering(self):
        """Test ordering books by publication year."""
        book2 = Book.objects.create(title="Order of the Phoenix", publication_year=2003, author=self.author)
        
        # Order ascending
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)
        self.assertEqual(response.data[1]['publication_year'], 2003)
