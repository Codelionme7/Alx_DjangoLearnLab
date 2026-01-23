# Django Advanced Features and Security

## Permissions and Groups Documentation

This project utilizes Django's permission system to enforce Role-Based Access Control (RBAC).

### Custom Permissions (bookshelf.models.Book)
The following custom permissions have been defined in `models.py`:
- `can_view`: Allows the user to view book instances.
- `can_create`: Allows the user to create new book instances.
- `can_edit`: Allows the user to edit existing book instances.
- `can_delete`: Allows the user to delete book instances.

### Groups Configuration
We have established the following groups in the Django Admin to manage these permissions:

1. **Viewers**
   - **Permissions:** `can_view`
   - **Role:** Read-only access to library content.

2. **Editors**
   - **Permissions:** `can_view`, `can_create`, `can_edit`
   - **Role:** Can create and update content but cannot delete.

3. **Admins**
   - **Permissions:** `can_view`, `can_create`, `can_edit`, `can_delete`
   - **Role:** Full administrative control over the library.

### Implementation Details
- **Views:** Access to views is restricted using the `@permission_required` decorator.
- **Example:** The `edit_book` view checks for `bookshelf.can_edit`.
