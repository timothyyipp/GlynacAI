from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import timedelta

from employees.models import Employee
from department.models import Department
from performance.models import Performance
from attendance.models import Attendance

class Command(BaseCommand):
    """
    Django management command to seed the database with fake data for employees, departments,
    performance reviews, and attendance records.
    This command performs the following actions:
    - Deletes all existing Attendance, Performance, Employee, and Department records.
    - Creates a predefined set of departments.
    - Generates a random number (between 30 and 50) of employees, each assigned to a random department.
    - For each employee, creates between 1 and 5 performance review records with random ratings and review dates.
    - For each employee, generates attendance records for approximately the last 3 months (weekdays only),
        with a 90% chance of attendance per day and random attendance status ('P' for present, 'A' for absent, 'L' for late).
    Intended for development and testing purposes to populate the database with realistic sample data.
    """
    help = 'Seed the database with fake employees, departments, performance, and attendance data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear old data
        Attendance.objects.all().delete()
        Performance.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()

        # Create Departments
        department_names = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance']
        departments = [Department.objects.create(name=name) for name in department_names]

        # Create Employees
        num_employees = random.randint(30, 50)
        employees = []

        for _ in range(num_employees):
            emp = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone=fake.msisdn()[:20],
                address=fake.address(),
                date_joined=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(departments)
            )
            employees.append(emp)

        # Create Performance records
        for emp in employees:
            num_reviews = random.randint(1, 5)
            for _ in range(num_reviews):
                review_date = fake.date_between(start_date=emp.date_joined, end_date='today')
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=review_date,
                )

        # Create Attendance records
        attendance_statuses = ['P', 'A', 'L']
        days_to_seed = 90  # last 3 months approx.

        for emp in employees:
            # Pick a random start date within last 3 months for attendance
            start_date = fake.date_between(start_date='-3m', end_date='-2m')

            # Generate unique attendance dates on weekdays only
            attendance_dates = []
            current_date = start_date
            while len(attendance_dates) < days_to_seed:
                if current_date.weekday() < 5:  # Monday=0 ... Friday=4 are weekdays
                    attendance_dates.append(current_date)
                current_date += timedelta(days=1)

            # Create attendance records for these dates with random status
            for att_date in attendance_dates:
                # 90% chance to create a record for that day
                if random.random() <= 0.9:
                    Attendance.objects.create(
                        employee=emp,
                        date=att_date,
                        status=random.choices(attendance_statuses, weights=[85, 10, 5])[0]
                    )

        self.stdout.write(self.style.SUCCESS(
            f'Successfully seeded {num_employees} employees, '
            f'{len(departments)} departments, '
            f'performance reviews, and attendance records.'
        ))
