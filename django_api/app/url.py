from django.urls import path
from .views import MercadoLibreAuthURL, MercadoLibreCallback, MercadoLibrePublish

urlpatterns = [
    path('auth-url/<str:client_id>/', MercadoLibreAuthURL.as_view(), name='auth-url'),
    path('callback/', MercadoLibreCallback.as_view(), name='callback'),
    path('publish/<str:client_id>/', MercadoLibrePublish.as_view(), name='publish'),
]
