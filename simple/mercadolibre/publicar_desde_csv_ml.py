
import requests
import csv

# 🔐 Access Token generado previamente
ACCESS_TOKEN = 'TU_ACCESS_TOKEN'  # ⬅️ Reemplazar con el token válido

# 📂 Archivo CSV con los productos (en la misma carpeta del script)
CSV_FILE = 'plantilla_publicacion_mercadolibre.csv'

# 📌 URL de la API de MercadoLibre
url = "https://api.mercadolibre.com/items"

# 📤 Headers
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# 📖 Leer CSV y publicar cada producto
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        producto = {
            "title": row["title"],
            "price": float(row["price"]),
            "currency_id": row["currency_id"],
            "category_id": row["category_id"],
            "available_quantity": int(row["available_quantity"]),
            "buying_mode": row["buying_mode"],
            "listing_type_id": row["listing_type_id"],
            "condition": row["condition"],
            "description": {
                "plain_text": row["description"]
            },
            "pictures": [
                {
                    "source": row["image_url"]
                }
            ],
            "attributes": [
                {
                    "id": "BRAND",
                    "value_name": row["brand"]
                },
                {
                    "id": "MODEL",
                    "value_name": row["model"]
                }
            ]
        }

        response = requests.post(url, json=producto, headers=headers)
        if response.status_code == 201:
            data = response.json()
            print("✅ Publicado:", data["title"])
            print("🔗 URL:", data["permalink"])
        else:
            print("❌ Error al publicar:", row["title"])
            print(response.status_code, response.text)
