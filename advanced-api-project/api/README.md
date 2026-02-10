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

- ## Testing Strategy

The `api/test_views.py` file contains unit tests for the Book API. 
We use `APITestCase` to simulate HTTP requests and check responses.

### Key Scenarios Tested:
1.  **Authentication:** Verified that unauthenticated users cannot Create, Update, or Delete books (401 Unauthorized), but can View them (200 OK).
2.  **CRUD Operations:** Verified that valid data creates/updates records correctly and invalid data or permissions are handled.
3.  **Filtering:** Verified that `?title=` parameters correctly filter the queryset.
4.  **Searching:** Verified that `?search=` parameters return matching results.
5.  **Ordering:** Verified that `?ordering=` parameters sort the response data correctly.
