from django.shortcuts import render
from .serializers import SupplySerializer
from rest_framework import viewsets, mixins
from .models import Supply


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
