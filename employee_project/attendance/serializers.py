from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Attendance model.

    This serializer automatically includes all fields from the Attendance model.
    It is used to convert Attendance model instances to and from JSON representations,
    facilitating serialization and deserialization in API endpoints.

    Attributes:
        Meta (class): Configuration for the serializer, specifying the model and fields to include.
    """
    class Meta:
        model = Attendance
        fields = '__all__'
