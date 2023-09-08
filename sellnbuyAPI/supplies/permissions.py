"""
Object-level permission to only allow owners of an object to edit it.
Assumes the model instance has an `owner` attribute.
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def permission(self, request, view):
        return request.method in permissions.SAFE_METHODS and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.method in permissions.SAFE_METHODS
