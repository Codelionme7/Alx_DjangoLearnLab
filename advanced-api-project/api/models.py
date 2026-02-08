from django.db import models

class Author(models.Model):
    """
    Represents an author entity.
    Field:
    - name: The name of the author.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book entity associated with an author.
    Fields:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: Foreign key to Author. Using related_name='books' allows
      accessing an author's books via author.books.all().
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
