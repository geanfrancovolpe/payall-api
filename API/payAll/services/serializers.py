# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Service, Category, Group

from files.serializers import MediaFileSerializer
from users.serializers import CustomUserSerializer


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ServicesSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['name', 'image', 'categories']

class ServicesDetailSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    service = ServicesSerializer(many=False, read_only=True)
    
    class Meta:
        model = Group
        fields = ['title', 'service', 'group_image']


class GroupDetailsSerializer(serializers.ModelSerializer):
    service = ServicesDetailSerializer(many=False, read_only=True)
    files = MediaFileSerializer(many=True, read_only=True)
    users = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'