# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Service, Category, Group


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ServicesSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    service = ServicesSerializer(many=False, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'