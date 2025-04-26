import requests

ACCESS_TOKEN = 'APP_USR-2174482344174560-041723-3b06c9bcfd810bd3cdf3f126f488b2dd-90290344'
url = "https://api.mercadolibre.com/items"

producto = {
    "title": "Chromecast HD - Publicado desde Python 🚀",
    "price": 35000,
    "currency_id": "ARS",
    "category_id": "MLA3530",
    "available_quantity": 1,
    "buying_mode": "buy_it_now",
    "listing_type_id": "gold_special",
    "condition": "new",
    "description": {
        "plain_text": "Streaming con Google TV, control por voz, resolución Full HD. Publicado desde un script automático."
    },
    "pictures": [
        {
            "source": "https://http2.mlstatic.com/D_NQ_NP_2X_687059-MLA54938587589_042023-F.jpg"
        }
    ],
    "attributes": [
        {
            "id": "BRAND",
            "value_name": "Google"
        },
        {
            "id": "MODEL",
            "value_name": "Chromecast HD"
        }
    ]
}

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=producto, headers=headers)

if response.status_code == 201:
    item = response.json()
    print("✅ Producto publicado correctamente")
    print("🆔 ID:", item["id"])
    print("🔗 URL:", item["permalink"])
else:
    print("❌ Error al publicar:")
    print(response.status_code)
    print(response.text)
