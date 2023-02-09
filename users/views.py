from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer

# from .serializers import CustomPasswordResetSerializer
from .models import CustomUser

# Create your views here.
# class PasswordResetView(GenericAPIView):
#     serializer_class = CustomPasswordResetSerializer
#     permission_classes = (AllowAny,)

#     def post(self, request, *args, **kwargs):
#         get_object_or_404(CustomUser, email=request.data.get("email"))

#         # Create a serializer with request.data
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         serializer.save()
#         # Return the success message with OK HTTP status
#         return Response(
#             {"detail": u"Password reset e-mail has been sent."},
#             status=status.HTTP_200_OK
#         )

class ContactListRetrieve(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def list(self, request, *args, **kwargs):
        queryset = request.user.contacts.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



