from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination
from attendance.models import Attendance
from django.db.models import Count
from django.db.models.functions import TruncMonth

# Create your views here.

# Pagination for API
class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

# API ViewSet for Employees
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['department', 'date_joined']
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['date_joined', 'first_name', 'last_name']

# HTML View for Charts
def charts_view(request):
    """
    Renders a dashboard view with charts data for employees and attendance.
    This view prepares data for two charts:
    1. Employees per Department: Aggregates the number of employees in each department.
    2. Monthly Attendance Overview: Aggregates the number of attendance records per month.
    Context passed to the template:
    - department_labels: List of department names.
    - department_counts: List of employee counts per department.
    - month_labels: List of month labels in 'Mon YYYY' format.
    - monthly_counts: List of attendance counts per month.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered 'charts.html' template with chart data context.
    """
    # Employees per Department
    dept_data = (
        Employee.objects.values('department__name')
        .annotate(count=Count('id'))
        .order_by('department__name')
    )
    department_labels = [item['department__name'] for item in dept_data]
    department_counts = [item['count'] for item in dept_data]

    # Monthly Attendance Overview
    monthly_attendance = (
        Attendance.objects.annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    month_labels = [item['month'].strftime('%b %Y') for item in monthly_attendance]
    monthly_counts = [item['count'] for item in monthly_attendance]

    return render(request, 'charts.html', {
        'department_labels': department_labels,
        'department_counts': department_counts,
        'month_labels': month_labels,
        'monthly_counts': monthly_counts,
    })