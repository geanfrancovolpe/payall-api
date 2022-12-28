from rest_framework.viewsets import ModelViewSet

from .models import Service, Group
from .serializers import GroupSerializer, ServicesSerializer, GroupDetailsSerializer

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_serializer_class(self):
        return GroupDetailsSerializer if self.action == 'retrieve' else GroupSerializer

    def list(self, request, *args, **kwargs):
        retrieve_shared = request.query_params.get("type") == "shared-services"
        self.queryset = (self.queryset.filter(users__id=request.user.id) if 
                        retrieve_shared else self.queryset.filter(user=request.user))
        return super().list(request)

    
class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer