# Advanced Features and Security - Django Project

This project implements advanced Django features including a custom user model, role-based access control, and security best practices.

## 1. Custom User Model
We have replaced the default Django User model with `bookshelf.CustomUser`.
- **Fields Added**:
  - `date_of_birth`: DateField
  - `profile_photo`: ImageField
- **Manager**: `CustomUserManager` handles user creation with these new fields.

## 2. Permissions and Groups
We utilize Django's permission system to restrict access to specific actions on the `Book` model.

### Custom Permissions defined in `models.py`:
- `bookshelf.can_view`: Allows a user to view the list of books.
- `bookshelf.can_create`: Allows a user to create new book entries.
- `bookshelf.can_edit`: Allows a user to modify existing book entries.
- `bookshelf.can_delete`: Allows a user to remove book entries.

### Groups Configuration:
To set up access control, the following groups should be created in the Django Admin:

1.  **Viewers**
    - Permissions: `can_view`
    - Role: Read-only access to book lists.

2.  **Editors**
    - Permissions: `can_view`, `can_create`, `can_edit`
    - Role: Can manage book content but cannot delete entries.

3.  **Admins**
    - Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`
    - Role: Full control over book entries.

## 3. Usage
- **Views**: The views in `bookshelf/views.py` are protected using the `@permission_required` decorator.
  - Example: `@permission_required('bookshelf.can_edit', raise_exception=True)` ensures only users with the `can_edit` permission can access the edit page.
- **Testing**:
  1. Create a user via the Admin panel.
  2. Assign the user to a group (e.g., "Editors").
  3. Attempt to access restricted URLs (e.g., `/books/create/`). Access should be granted or denied based on the group's permissions.
