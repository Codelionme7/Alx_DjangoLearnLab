from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create an author
        self.author = Author.objects.create(name="Author One")
        
        # Create some books
        self.book1 = Book.objects.create(
            title="Book One",
            publication_year=2020,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            publication_year=2021,
            author=self.author
        )

        # URLs
        self.list_url = '/api/books/'
        self.create_url = '/api/books/create/'
        
    def test_list_books(self):
        """Test retrieving list of books (Public access)"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        """Test creating a book with authentication"""
        self.client.login(username='testuser', password='password')
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication (Should fail)"""
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book(self):
        """Test updating a book"""
        self.client.login(username='testuser', password='password')
        update_url = f'/api/books/update/{self.book1.id}/'
        data = {'title': 'Updated Title', 'publication_year': 2020, 'author': self.author.id}
        response = self.client.put(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.login(username='testuser', password='password')
        delete_url = f'/api/books/delete/{self.book1.id}/'
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """Test filtering books by title"""
        response = self.client.get(self.list_url + '?title=Book One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_search_books(self):
        """Test searching books"""
        response = self.client.get(self.list_url + '?search=One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')
        
    def test_ordering_books(self):
        """Test ordering books by publication year"""
        response = self.client.get(self.list_url + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One') # 2020 comes before 2021
