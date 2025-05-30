from django.urls import path, include
"""
URL configuration for the attendance app.
This module sets up routing for the AttendanceViewSet using Django REST Framework's DefaultRouter.
All routes for attendance-related API endpoints are automatically generated and included at the root path.
Routes:
    '' : Includes all routes registered with the DefaultRouter for AttendanceViewSet.
Imports:
    - path, include: Django URL utilities.
    - DefaultRouter: DRF router for viewsets.
    - AttendanceViewSet: ViewSet handling attendance logic.
"""
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet

router = DefaultRouter()
router.register('', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]