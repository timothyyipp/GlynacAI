from django.urls import path, include
"""
URL configuration for the employees app.
- Registers a DRF DefaultRouter for EmployeeViewSet, exposing standard RESTful endpoints for employee resources.
- Includes a custom path 'charts/' mapped to the charts_view for additional data visualization or analytics.
Routes:
    ''         : EmployeeViewSet endpoints (list, create, retrieve, update, delete employees)
    'charts/'  : charts_view endpoint for employee-related charts or analytics
Imports:
    - path, include: Django URL utilities
    - DefaultRouter: DRF router for viewsets
    - EmployeeViewSet, charts_view: Local views to be routed
"""
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, charts_view

router = DefaultRouter()
router.register('', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('charts/', charts_view, name='charts'),
]
