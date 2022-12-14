from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Service, Group
from .serializers import GroupSerializer, ServicesSerializer

# Create your views here.
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer