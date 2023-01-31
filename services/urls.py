from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, ServiceViewSet, CatergoryViewSet

urlpatterns = []
router = DefaultRouter()
router.register(r"service", ServiceViewSet, basename="service")
router.register(r"group", GroupViewSet, basename="group")
router.register(r"category", CatergoryViewSet, basename="category")

urlpatterns += router.urls