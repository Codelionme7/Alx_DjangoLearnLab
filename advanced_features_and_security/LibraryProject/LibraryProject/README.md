# Django Advanced Features and Security

## Permissions and Groups Setup
This project uses custom permissions on the `Book` model to control access.

### Custom Permissions
The following permissions were defined in `models.py`:
- `bookshelf.can_view`: Permission to view the list of books.
- `bookshelf.can_create`: Permission to create new books.
- `bookshelf.can_edit`: Permission to edit existing books.
- `bookshelf.can_delete`: Permission to delete books.

### Groups
We have established the following groups in the Django Admin:
1. **Viewers**: Assigned `can_view`.
2. **Editors**: Assigned `can_view`, `can_create`, `can_edit`.
3. **Admins**: Assigned `can_view`, `can_create`, `can_edit`, `can_delete`.

### Testing
To test, log in with users assigned to these groups and attempt to access the protected views in `views.py`.


# Security & Permissions Setup

## Custom User Model
Using `bookshelf.CustomUser` with `date_of_birth` and `profile_photo`.

## Permissions & Groups
Defined in `bookshelf/models.py`:
- `can_view`, `can_create`, `can_edit`, `can_delete`
Groups (Viewers, Editors, Admins) should be created in Admin panel.

## Security Features
- **CSRF**: All forms use `{% csrf_token %}`.
- **XSS/CSP**: Headers configured in settings.
- **HTTPS**: `SECURE_SSL_REDIRECT` and HSTS enabled.
- **Secure Views**: `@permission_required` enforces access control.
