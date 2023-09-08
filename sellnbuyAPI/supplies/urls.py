from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplyViewSet, CommentViewSet, MessageViewSet

router = DefaultRouter()

router.register('supply', SupplyViewSet, basename='supplies')
router.register('supply/(?P<id>\d+)/comment', CommentViewSet, basename='comment')
router.register('send-message', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls))
]
