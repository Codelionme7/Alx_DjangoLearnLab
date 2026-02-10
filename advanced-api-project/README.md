# Advanced API Project Documentation

## View Configurations (`api/views.py`)

This API uses Django REST Framework's generic views to handle CRUD operations for the `Book` model.

### 1. ListView (`BookListView`)
- **Type:** `ListAPIView`
- **Purpose:** Retrieves a list of all books.
- **Permissions:** `IsAuthenticatedOrReadOnly` (Public Read access).

### 2. DetailView (`BookDetailView`)
- **Type:** `RetrieveAPIView`
- **Purpose:** Retrieves details of a specific book by ID.
- **Permissions:** `IsAuthenticatedOrReadOnly` (Public Read access).

### 3. CreateView (`BookCreateView`)
- **Type:** `CreateAPIView`
- **Purpose:** Adds a new book to the database.
- **Permissions:** `IsAuthenticated` (Requires login).
- **Customization:** The `perform_create` method is overridden to handle custom save logic.

### 4. UpdateView (`BookUpdateView`)
- **Type:** `UpdateAPIView`
- **Purpose:** Modifies an existing book.
- **Permissions:** `IsAuthenticated` (Requires login).
- **Customization:** The `perform_update` method is overridden to handle custom update logic.

### 5. DeleteView (`BookDeleteView`)
- **Type:** `DestroyAPIView`
- **Purpose:** Removes a book from the database.
- **Permissions:** `IsAuthenticated` (Requires login).
