from django.contrib import admin
from .models import Book

# Customizing the Admin interface
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for these fields in the right sidebar
    list_filter = ('author', 'publication_year')
    
    # Enable a search bar to search by title or author
    search_fields = ('title', 'author')

# Register the model with the custom configuration
admin.site.register(Book, BookAdmin)