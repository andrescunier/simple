from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InscripcionViewSet

router = DefaultRouter()
router.register(r'inscripciones', InscripcionViewSet, basename='inscripciones')

urlpatterns = [
    path('', include(router.urls)),
]
