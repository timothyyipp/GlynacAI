from django.db import models
from department.models import Department

# Create your models here.
class Employee(models.Model):
    """
    Represents an employee within the organization.
    Fields:
        first_name (CharField): The employee's first name.
        last_name (CharField): The employee's last name.
        email (EmailField): The employee's unique email address.
        phone (CharField): The employee's phone number.
        address (TextField): The employee's residential address.
        date_joined (DateField): The date the employee joined the organization.
        department (ForeignKey): Reference to the Department the employee belongs to.
    Methods:
        __str__(): Returns the full name of the employee.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_joined = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"