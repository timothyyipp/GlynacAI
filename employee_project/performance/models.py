from django.db import models
from employees.models import Employee

# Create your models here.
class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    rating = models.IntegerField()  # Expected 1 to 5
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.rating} on {self.review_date}"