from django.urls import path, include
"""
URL configuration for the department app.
This module sets up routing for the DepartmentViewSet using Django REST Framework's DefaultRouter.
All routes for department-related API endpoints are automatically generated and included at the root path.
Routes:
    - All CRUD operations for departments are available via the registered DepartmentViewSet.
Usage:
    Include this urls.py in the project's main URL configuration to expose department API endpoints.
"""
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet

router = DefaultRouter()
router.register('', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
