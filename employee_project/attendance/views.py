from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Attendance
from .serializers import AttendanceSerializer

# Create your views here.
class AttendanceViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Attendance instances.

    This viewset provides standard CRUD actions for the Attendance model, including filtering, searching, and ordering capabilities.

    Attributes:
        queryset (QuerySet): All Attendance objects.
        serializer_class (Serializer): Serializer for Attendance objects.
        filter_backends (list): List of filter backends for filtering, searching, and ordering.
        filterset_fields (list): Fields that can be filtered (employee, date).
        search_fields (list): Fields that can be searched (employee's first and last name).
        ordering_fields (list): Fields that can be used for ordering (date, employee).
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['employee', 'date']
    search_fields = ['employee__first_name', 'employee__last_name']
    ordering_fields = ['date', 'employee']