from django.shortcuts import render, get_object_or_404
from .serializers import SupplySerializer, CommentSerializer
from rest_framework import viewsets, mixins
from .models import Supply, Comment


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        supply = get_object_or_404(Supply, id=self.kwargs.get('id'))
        return Comment.objects.filter(supply=supply)

    def perform_create(self, serializer):
        supply = get_object_or_404(Supply, id=self.kwargs.get('id'))
        serializer.save(user=self.request.user, supply=supply)
    
