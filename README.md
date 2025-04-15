# Auth System

A Django REST API for managing users, roles, and permissions.

## Features
- Token-based authentication
- User login for admins and regular users
- Full CRUD for:
  - Users
  - Roles
  - Permissions
- Assign roles to users
- Assign permissions to roles
- Swagger UI documentation at `/swagger/`

## Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/tylerriverbay/auth_system.git
   cd auth_system

2. Create/activate virtual environment
    python -m venv venv
    source venv/bin/activate      # macOS/Linux
    venv\Scripts\activate         # Windows

3. Install dependencies
    pip install -r requirements.txt

4. Run migrations
    python manage.py migrate

5. Start server
    python manage.py runserver

6. http://127.0.0.1:8000/swagger/  - Swagger UI
   http://127.0.0.1:8000/admin/    - Django Admin Page
   http://127.0.0.1:8000/api/user/login/
   http://127.0.0.1:8000/api/admin/login/

   Sign in with user/admin account and copy token to authorize on Swagger UI. Enter token like this: Token your_token_here

   GET/POST/PUT/DELETE /api/users/ – User management
   GET/POST/PUT/DELETE /api/roles/ – Role management (admin, user, etc)
   GET/POST/PUT/DELETE /api/permissions/ – Permission management

   Note:
    Modifying or deleting default Django permissions may affect admin access or app behavior.
    It's recommended to only create/edit/delete **custom permissions** unless you know what you're doing.
