from django.core.management.base import BaseCommand
from faker import Faker
import random

from employees.models import Employee
from department.models import Department

class Command(BaseCommand):
    help = 'Seed the database with fake employees and departments'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Optional: Clear old data
        Employee.objects.all().delete()
        Department.objects.all().delete()

        # Create Departments
        department_names = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance']
        departments = []

        for name in department_names:
            dept = Department.objects.create(name=name)
            departments.append(dept)

        # Create Employees
        num_employees = random.randint(30, 50)

        for _ in range(num_employees):
            Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.msisdn()[:20],
                address=fake.address(),
                date_joined=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(departments)
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {num_employees} employees across {len(departments)} departments!'))
