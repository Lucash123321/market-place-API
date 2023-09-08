from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplyViewSet, CommentViewSet, MessageViewSet

router = DefaultRouter()

router.register('supplies', SupplyViewSet, basename='supplies')
router.register('supplies/(?P<id>\d+)/comments', CommentViewSet, basename='comments')
router.register('send-message', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls))
]
