# API Documentation

## BookListView Features

We have implemented advanced query capabilities using Django REST Framework's filter backends.

### 1. Filtering
Allows exact matching against specific fields.
- **Backend:** `DjangoFilterBackend`
- **Fields:** `title`, `author`, `publication_year`
- **Usage:** `/books/?author__name=Orwell`

### 2. Searching
Allows partial text search across specified fields.
- **Backend:** `SearchFilter`
- **Fields:** `title`, `author`
- **Usage:** `/books/?search=1984`

### 3. Ordering
Allows sorting results. Default is ascending; prefix with `-` for descending.
- **Backend:** `OrderingFilter`
- **Fields:** `title`, `publication_year`
- **Usage:** `/books/?ordering=-publication_year`
