from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Performance
from .serializers import PerformanceSerializer

# Create your views here.
class PerformanceViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Performance instances.

    This viewset provides the following features:
    - Lists, retrieves, creates, updates, and deletes Performance records.
    - Supports filtering by 'employee' and 'review_date' fields.
    - Allows searching by employee's first and last name.
    - Enables ordering by 'score' and 'review_date'.

    Attributes:
        queryset: Queryset of all Performance objects.
        serializer_class: Serializer class for Performance objects.
        filter_backends: List of filter backends for filtering, ordering, and searching.
        filterset_fields: Fields available for filtering.
        search_fields: Fields available for search queries.
        ordering_fields: Fields available for ordering results.
    """
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['employee', 'review_date']
    search_fields = ['employee__first_name', 'employee__last_name']
    ordering_fields = ['score', 'review_date']