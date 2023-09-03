from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplyViewSet, CommentViewSet

router = DefaultRouter()

router.register('supply', SupplyViewSet, basename='supplies')
router.register('supply/<int:id>', SupplyViewSet, basename='supply')
router.register('supply/(?P<id>\d+)/comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls))
]
'''
urlpatterns = [
    path('', views.main, name='index'),
    path('add-supply/', views.add_supply, name='add_supply'),
    path('messanger', views.messanger, name='messanger'),
    path('<int:id>/', views.view_supply, name='supply'),
    path('<int:id>/comment', views.add_comment, name='add_comment'),
    path('change-supply/<int:id>', views.change_supply, name='change_supply'),
    path('delete-supply/<int:id>', views.delete_supply, name='delete_supply'),
    path('change-comment/<int:id>', views.change_comment, name='change_comment'),
    path('delete-comment/<int:id>', views.delete_comment, name='delete_comment'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/chat', views.open_chat, name='chat'),
    path('<str:username>/chat/send-message', views.send_message, name='send_message'),
    ]
'''

