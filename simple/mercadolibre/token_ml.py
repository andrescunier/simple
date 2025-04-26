
import requests

# 🔐 Datos reales
CLIENT_ID = '2174482344174560'
CLIENT_SECRET = 'rQkBy8fOZyHeSTpYymJGPjvGPklBawJ9'
AUTHORIZATION_CODE = 'TG-6801cab910016a00013da7b3-90290344'
REDIRECT_URI = 'https://httpbin.org/get'

# 🌐 URL de token
url = "https://api.mercadolibre.com/oauth/token"

# 📦 Datos para la solicitud
data = {
    "grant_type": "authorization_code",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "code": AUTHORIZATION_CODE,
    "redirect_uri": REDIRECT_URI
}

# 🚀 Solicitud POST
response = requests.post(url, data=data)

# 📋 Mostrar resultado
if response.status_code == 200:
    tokens = response.json()
    print("✅ Access Token:", tokens["access_token"])
    print("🔁 Refresh Token:", tokens["refresh_token"])
    print("⏳ Expira en:", tokens["expires_in"], "segundos")
    print("🧑‍💼 User ID:", tokens.get("user_id"))
else:
    print("❌ Error al obtener token:")
    print(response.status_code)
    print(response.text)
