from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, ServiceViewSet 

urlpatterns = []
router = DefaultRouter()
router.register(r"service", ServiceViewSet, basename="service")
router.register(r"group", GroupViewSet, basename="group")

urlpatterns += router.urls