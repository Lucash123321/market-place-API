from rest_framework import serializers
from .models import Supply, Comment, Message
from django.shortcuts import get_object_or_404


class SupplySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Supply
        fields = ('user', 'name', 'price', 'desc', 'image')
        read_only_fields = ('user', )


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ('user', 'rating', 'supply', 'text',)
        read_only_fields = ('user', 'supply')

    def validate(self, attrs):
        supply = get_object_or_404(Supply, id=self.context['view'].kwargs.get('id'))
        comment_exist = Comment.objects.filter(supply=supply)
        if comment_exist:
            raise serializers.ValidationError
        return attrs
