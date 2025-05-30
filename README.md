# GlynacAI Setup Guide

## 1. Install Dependencies

```bash
pip install django djangorestframework drf-yasg django-environ Faker django-filter psycopg2-binary djangorestframework-simplejwt
```

---

## 2. Start Django Project

```bash
django-admin startproject employee_project
```

---

## 3. Create Django Apps

```bash
python manage.py startapp employees
python manage.py startapp attendance
python manage.py startapp department
python manage.py startapp performance
```

---

## 4. Configure PostgreSQL Database

Run these SQL commands in your PostgreSQL client:

```sql
CREATE DATABASE employee;
CREATE USER employees WITH PASSWORD 'welcome';
ALTER ROLE employees SET client_encoding TO 'utf8';
ALTER ROLE employees SET default_transaction_isolation TO 'read committed';
ALTER ROLE employees SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE employee TO employees;
GRANT ALL PRIVILEGES ON SCHEMA public TO employees;
```

If you encounter permission issues during migrations, run the following in PGAdmin:

```sql
GRANT ALL ON SCHEMA public TO employees;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO employees;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO employees;
```

---

## 5. Create `.env` File

- Place the `.env` file in the same directory as `manage.py`.
- Refer to `.env.example` for the required variables.

---

## 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7. Seed the Database

```bash
python manage.py seed_employees
```

---

## 8. Create Superuser
You will be prompted to create an account (you can ignore email)

```bash
python manage.py createsuperuser
```

---

## 9. Run the Development Server

```bash
python manage.py runserver
```

---

## 10. Access the Application

- Open [http://localhost:8000/swagger/](http://localhost:8000/swagger/) in your browser.
- Log in using your superuser credentials to access the API endpoints.
