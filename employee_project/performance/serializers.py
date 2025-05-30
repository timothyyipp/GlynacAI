from rest_framework import serializers
from .models import Performance

class PerformanceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Performance model.

    This serializer automatically includes all fields from the Performance model.
    It is used to convert Performance model instances to and from JSON representations,
    enabling easy serialization and deserialization of Performance data in API views.

    Attributes:
        Meta (class): Configuration for the serializer, specifying the model and fields to include.
    """
    class Meta:
        model = Performance
        fields = '__all__'
