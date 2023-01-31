from rest_framework.viewsets import ModelViewSet
from django.db.models import Q

from .models import Service, Group, Category
from .serializers import GroupSerializer, ServicesSerializer, GroupDetailsSerializer, CategoriesSerializer

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

    def list(self, request, *args, **kwargs):
        filter_by = request.query_params.get("filter", None)
        if filter_by:
            self.queryset = Service.objects.filter(Q(name__icontains=filter_by) | Q(categories__name__icontains=filter_by))

        return super().list(request)

class CatergoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer