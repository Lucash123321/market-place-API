from rest_framework import serializers
from .models import Supply, Comment, Message


class SupplySerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Supply
        fields = ('user', 'name', 'price', 'desc', 'image')
        read_only_fields = ('user', )

