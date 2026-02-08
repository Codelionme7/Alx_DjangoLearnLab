from django.db import models

class Author(models.Model):
    """
    The Author model represents a writer of books.
    
    Fields:
    - name: The name of the author (CharField).
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model represents a literary work linked to an author.
    
    Fields:
    - title: The title of the book (CharField).
    - publication_year: The year the book was published (IntegerField).
    - author: A foreign key to the Author model. 
              'related_name' allows accessing books from an author instance (e.g., author.books.all()).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
