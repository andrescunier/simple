from django.db import models

class MarketplaceCredential(models.Model):
    client_name = models.CharField(max_length=255)
    marketplace = models.CharField(max_length=50, default='mercadolibre')
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    token_expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client_name} - {self.marketplace}"
