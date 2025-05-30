from django.db import models
from employees.models import Employee

# Create your models here.
class Performance(models.Model):
    """
    Represents an employee's performance review.
    Fields:
        employee (ForeignKey): Reference to the Employee being reviewed.
        rating (IntegerField): Performance rating, expected to be between 1 and 5.
        review_date (DateField): The date the performance review was conducted.
    Methods:
        __str__(): Returns a string representation of the performance review, including the employee's name, rating, and review date.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    rating = models.IntegerField()  # Expected 1 to 5
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.rating} on {self.review_date}"