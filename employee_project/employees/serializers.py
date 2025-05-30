from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee model.

    This serializer automatically generates fields for all attributes of the Employee model,
    enabling serialization and deserialization of Employee instances to and from JSON or other formats.

    Attributes:
        Meta (class): Specifies the model to serialize (Employee) and includes all fields.

    Usage:
        Used in views to convert Employee model instances to JSON and validate incoming data for Employee creation or update.
    """
    class Meta:
        model = Employee
        fields = '__all__'