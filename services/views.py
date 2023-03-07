
from django.db.models import Q
from django.http import JsonResponse

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404

from .models import Service, Group, Category, InvitedUser
from .serializers import GroupSerializer, ServicesSerializer, GroupDetailsSerializer, CategoriesSerializer, InvitedUserSerializer, \
    GroupDetailsSerializer, GroupSmallDetailSerializer

class GroupViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Group.objects.all()
    serializer_class = GroupSmallDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return GroupDetailsSerializer
        
        if self.action in ["create", "update"]:
            return GroupSerializer
        
        return self.serializer_class

    def list(self, request, *args, **kwargs):
        retrieve_shared = request.query_params.get("type") == "shared-services"
        self.queryset = (self.queryset.filter(users__id=request.user.id) if 
                        retrieve_shared else self.queryset.filter(user=request.user))
        return super().list(request)

    @action(detail=False, methods=['post'], url_path="invited-users")
    def invited_users_add(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        invited_user_serializer = InvitedUserSerializer(data=request.data)
        if invited_user_serializer.is_valid(raise_exception=True):
            InvitedUser.objects.update_or_create(
                email=invited_user_serializer.validated_data["email"],
                defaults=invited_user_serializer.validated_data
            )
            return JsonResponse(invited_user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse("Error de invitación", status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], url_path="invited-users-list/(?P<pk>[^/.]+)")
    def invited_users_list(self, request, pk=None):
        group = get_object_or_404(Group, pk=pk)
        serialized_queryset = InvitedUserSerializer(group.invitations, many=True)
        return JsonResponse(serialized_queryset.data, status=status.HTTP_200_OK, safe=False) 

    @action(detail=False, methods=['post'], url_path="check-existing")
    def check_existing_group(self, request):
        existing_service = Group.check_existing_group(request.user, request.data["service"])
        if existing_service:
            return JsonResponse(
                {"group": GroupDetailsSerializer(existing_service).data, "exists": True}, 
                status=status.HTTP_200_OK, 
                safe=False
            ) 
        return JsonResponse({"group": None, "exists": False})
    
    @action(detail=True, methods=['post'], url_path="toggle-user")
    def toggle_user(self, request, pk):
        instance = self.get_object()
        user = request.data.get("user", None)
        if instance.users.filter(id=user).exists():
            instance.users.remove(user)
        else:
            instance.users.add(user)

        return JsonResponse(
            "Ok", 
            status=status.HTTP_200_OK, 
            safe=False
        ) 
        
    
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