from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import requests
from rest_framework import status
from django.utils.timezone import now, timedelta
from .models import MarketplaceCredential


class MercadoLibreAuthURL(APIView):
    def get(self, request, client_id):
        redirect_uri = settings.MERCADOLIBRE_REDIRECT_URI
        auth_url = (
            f"https://auth.mercadolibre.com.ar/authorization?"
            f"response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
        )
        return Response({"auth_url": auth_url})



class MercadoLibreCallback(APIView):
    def post(self, request):
        code = request.data.get('code')
        client_id = request.data.get('client_id')
        client_secret = request.data.get('client_secret')
        redirect_uri = settings.MERCADOLIBRE_REDIRECT_URI

        url = "https://api.mercadolibre.com/oauth/token"
        payload = {
            'grant_type': 'authorization_code',
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'redirect_uri': redirect_uri,
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            data = response.json()
            expires_in = data['expires_in']
            expires_at = now() + timedelta(seconds=expires_in)

            MarketplaceCredential.objects.update_or_create(
                client_id=client_id,
                defaults={
                    'client_secret': client_secret,
                    'access_token': data['access_token'],
                    'refresh_token': data['refresh_token'],
                    'token_expires_at': expires_at,
                }
            )
            return Response({"message": "Tokens guardados!"})
        else:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
class MercadoLibrePublish(APIView):
    def post(self, request, client_id):
        try:
            cred = MarketplaceCredential.objects.get(client_id=client_id)
        except MarketplaceCredential.DoesNotExist:
            return Response({"error": "No credentials found"}, status=404)

        url = "https://api.mercadolibre.com/items"
        headers = {
            "Authorization": f"Bearer {cred.access_token}"
        }
        product_data = request.data  # Chequeá la data que mandás desde Postman u otro

        response = requests.post(url, headers=headers, json=product_data)
        return Response(response.json(), status=response.status_code)
