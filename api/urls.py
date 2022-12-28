# api/urls.py
from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve


# from users.views import PasswordResetView
# from .views import FacebookLogin, GoogleLogin

urlpatterns = [
    path("users/", include("users.urls")),
    path("services/", include("services.urls")),
] 
