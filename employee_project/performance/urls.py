from django.urls import path, include
"""
URL configuration for the performance app.
This module sets up routing for the PerformanceViewSet using Django REST Framework's DefaultRouter.
All routes for the PerformanceViewSet are automatically generated and included at the root path.
Routes:
    '' : Includes all automatically generated routes for PerformanceViewSet.
Imports:
    - path, include: Django URL utilities.
    - DefaultRouter: DRF router for viewsets.
    - PerformanceViewSet: The viewset handling performance-related API endpoints.
"""
from rest_framework.routers import DefaultRouter
from .views import PerformanceViewSet

router = DefaultRouter()
router.register('', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
