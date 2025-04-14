# Auth System

A Django REST API for managing users, roles, and permissions.

## Features
- Token-based authentication
- User login for admins and regular users
- Full CRUD for:
  - Users
  - Roles
  - Permissions
- Swagger UI docs at `/swagger/`

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

To Do
    Link permissions to roles