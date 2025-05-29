# GlynacAI
1. Install Dependencies
```
pip install django djangorestframework drf-yasg django-environ Faker django-filter psycopg2-binary 
```

2. Start Django App
```
django-admin startproject employee_project
```

3. Create Apps
```
python manage.py startapp employees
python manage.py startapp attendance
python manage.py startapp department
python manage.py startapp performance
```

4. Create Database and Grant Permissions
```
CREATE DATABASE employee;
CREATE USER employees WITH PASSWORD 'welcome';
ALTER ROLE employees SET client_encoding TO 'utf8';
ALTER ROLE employees SET default_transaction_isolation TO 'read committed';
ALTER ROLE employees SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE employee TO employees;
GRANT ALL PRIVILEGES ON SCHEMA public TO employees;
```
(Had to run this in PGAdmin instead of psql terminal)
```
GRANT ALL ON SCHEMA public TO employees;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO employees;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO employees;
```

5. Create .env file <br/>
(Make sure it is in the same directory as manage.py) <br/>
(Look at .env.example for reference of what to put in)

```
python manage.py makemigrations
python manage.py migrate
```

6. Seeding the Database:
```
python manage.py seed_employees
```