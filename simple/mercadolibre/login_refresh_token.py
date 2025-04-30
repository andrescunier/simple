# login_continuo_mejorado.py

import requests
import json

# Configuración
CLIENT_ID = '2174482344174560'
CLIENT_SECRET = 'rQkBy8fOZyHeSTpYymJGPjvGPklBawJ9'
REDIRECT_URI = 'https://httpbin.org/get'

TOKEN_FILE = 'token_data.json'

def save_tokens(data):
    with open(TOKEN_FILE, 'w') as f:
        json.dump(data, f)

def load_tokens():
    try:
        with open(TOKEN_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def get_tokens_from_authorization_code(code):
    url = "https://api.mercadolibre.com/oauth/token"
    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json()

def refresh_access_token(refresh_token):
    url = "https://api.mercadolibre.com/oauth/token"
    payload = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": refresh_token
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json()

def main():
    tokens = load_tokens()

    if not tokens:
        print("No se encontró token guardado. Necesitamos un authorization_code.")
        code = input("Pegá aquí tu authorization_code: ")
        tokens = get_tokens_from_authorization_code(code)
        save_tokens(tokens)
        print("Tokens obtenidos y guardados exitosamente!")
    else:
        try:
            print("Intentando renovar access_token usando refresh_token...")
            tokens = refresh_access_token(tokens["refresh_token"])
            save_tokens(tokens)
            print("Access_token renovado exitosamente!")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 400:
                print("El refresh_token falló o expiró. Necesitamos un authorization_code nuevo.")
                code = input("Pegá aquí tu authorization_code: ")
                tokens = get_tokens_from_authorization_code(code)
                save_tokens(tokens)
                print("Tokens nuevos obtenidos y guardados exitosamente!")
            else:
                print("Error inesperado:", e)
                return

    print(f"\n✅ Access Token vigente:\n{tokens['access_token']}\n")

if __name__ == "__main__":
    main()
