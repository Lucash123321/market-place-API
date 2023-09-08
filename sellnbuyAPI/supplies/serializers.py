from rest_framework import serializers
from .models import Supply, Comment, Message, User
from django.shortcuts import get_object_or_404


class SupplySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Supply
        fields = ('user', 'name', 'price', 'desc', 'image')
        read_only_fields = ('user', )

    def validate(self, attrs):
        if not self.context['request'].user.is_authenticated:
            raise serializers.ValidationError
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ('user', 'rating', 'supply', 'text',)
        read_only_fields = ('user', 'supply')

    def validate(self, attrs):
        supply = get_object_or_404(Supply, id=self.context['view'].kwargs.get('id'))
        comment_exist = Comment.objects.filter(supply=supply)
        if not self.context['request'].user.is_authenticated or \
                comment_exist or supply.user == self.context['request'].user:
            raise serializers.ValidationError
        return attrs


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('user', 'to', 'time', 'text', )
        read_only_fields = ('user', 'time')

    def validate(self, attrs):
        user = get_object_or_404(User, username=attrs['to'])
        if self.context['request'].user == user:
            raise serializers.ValidationError
        return attrs
