from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, MeasurementCreateView

# TODO: зарегистрируйте необходимые маршруты

router = DefaultRouter()
router.register(r'sensors', SensorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('measurements/', MeasurementCreateView.as_view(), name='create-measurement'),
]
