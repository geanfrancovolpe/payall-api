# api/urls.py
from django.urls import include, path

# from users.views import PasswordResetView
# from .views import FacebookLogin, GoogleLogin


urlpatterns = [
    path("users/", include("users.urls")),
] 