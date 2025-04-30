# primer_login.py

import webbrowser

# Configurá tus datos de la app de Mercado Libre

CLIENT_ID = '2174482344174560'
REDIRECT_URI = 'https://httpbin.org/get'

def get_authorization_url():
    url = f"https://auth.mercadolibre.com.ar/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    return url

def main():
    url = get_authorization_url()
    print("Abrí este link para autorizar la app:")
    print(url)
    webbrowser.open(url)

if __name__ == "__main__":
    main()
