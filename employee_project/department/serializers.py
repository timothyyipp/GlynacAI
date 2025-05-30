from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Department model.

    This serializer automatically includes all fields from the Department model.
    It is used to convert Department model instances to and from JSON representations,
    typically for use in API endpoints.

    Attributes:
        Meta (class): Configuration for the serializer, specifying the model and fields to include.
    """
    class Meta:
        model = Department
        fields = '__all__'
