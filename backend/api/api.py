from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AppointmentViewSet, HealthRecordViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'healthrecords', HealthRecordViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
