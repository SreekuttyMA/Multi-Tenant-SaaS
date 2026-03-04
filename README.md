Multi-Tenant SaaS Platform
A Django-based multi-tenant SaaS application supporting user accounts, project management, and role-based permissions.

**Features**
Multi-tenant architecture
User authentication and management
Project CRUD operations
Role-based access control
RESTful API (Django REST Framework)
Redis caching

**Project Structure**
saas_project – Main Django project
core/ – Settings, URLs, WSGI/ASGI
accounts/ – User and authentication logic
projects/ – Project management, permissions, serializers
env – Python virtual environment

**Setup**

Clone the repository
git clone <repo-url>
cd Multi-Tenant-SaaS

Create and activate virtual environment
python -m venv env
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate

Install dependencies
pip install -r requirements.txt

Apply migrations
cd saas_project
python manage.py migrate

Run the development server
python manage.py runserver



**Usage**
Access the app at http://127.0.0.1:8000/
Use Django admin at /admin/
API endpoints available under /api/
