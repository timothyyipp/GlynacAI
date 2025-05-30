from django.db import models

# Create your models here.

class Department(models.Model):
    """
    Represents a department within the organization.
    Attributes:
        name (CharField): The name of the department, limited to 100 characters.
    Methods:
        __str__(): Returns the string representation of the department, which is its name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name