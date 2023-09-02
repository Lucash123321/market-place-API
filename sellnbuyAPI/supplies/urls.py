from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplyViewSet

router = DefaultRouter()

router.register('supply', SupplyViewSet, basename='supplies')
router.register('supply/<int:id>', SupplyViewSet, basename='supply')

urlpatterns = [
    path('', include(router.urls))
]

