
from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView
from .views import PasswordResetView

urlpatterns = [
    path("dj-rest-auth/password/reset/", PasswordResetView.as_view(), name='rest_password_reset'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path(
        'dj-rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', 
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    )
]
