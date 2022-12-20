from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Service, Group
from .serializers import GroupSerializer, ServicesSerializer, GroupDetailsSerializer

# Create your views here.
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_serializer_class(self):
        return GroupDetailsSerializer if self.action == 'retrieve' else GroupSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer