from django.shortcuts import render
from rest_framework import viewsets
from .models import Department
from .serializers import DepartmentSerializer

# Create your views here

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Department instances.

    This viewset provides default `list`, `create`, `retrieve`, `update`, and `destroy` actions
    for the Department model using the DepartmentSerializer.

    Attributes:
        queryset (QuerySet): The queryset of all Department objects.
        serializer_class (Serializer): The serializer class used for Department objects.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer