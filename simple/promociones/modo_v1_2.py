import requests
import json
import csv

def guardar_response_completo(response_text, filename="modo_response_completo.json"):
    """Guarda la respuesta completa del servidor en un archivo."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(response_text)
    print(f"Respuesta completa guardada en '{filename}'")

def obtener_datos():
    url = "https://rewards-handler.playdigital.com.ar/slots?slots=web-modo-hub-promos_corriendo,web-modo-hub-proximas_promos,web-modo-hub-promos_finalizadas&limit=25&page=1&source=web_modo&origin=web_modo&fcalcstatus=running,next_for_product,finished_for_product&search_ia=false"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.modo.com.ar/promos",
        "Origin": "https://www.modo.com.ar",
        "Cache-Control": "no-cache",
        "x-auth-application": "TU_TOKEN_AQUI"  # Reemplazar con tu token
    }
    
    try:
        session = requests.Session()
        response = session.get(url, headers=headers)
        print("Código de respuesta HTTP:", response.status_code)

        # Guardar la respuesta completa antes de procesarla
        guardar_response_completo(response.text, "modo_response_completo.json")

        if response.status_code != 200:
            print("Respuesta del servidor:", response.text)
            response.raise_for_status()
        
        try:
            data = response.json()
            print("Respuesta JSON recibida correctamente.")
        except json.JSONDecodeError:
            print("Error al decodificar la respuesta JSON.")
            return
        
        if "data" not in data or "cards" not in data["data"]:
            print("La estructura JSON no contiene 'data' -> 'cards'.")
            return
        
        cards = data["data"]["cards"]
        
        if not cards:
            print("No se encontraron tarjetas ('cards').")
            return
        
        # Guardar en CSV
        with open("modo_datos.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            # Escribir encabezados basados en las claves del primer objeto
            headers = cards[0].keys()
            writer.writerow(headers)
            
            # Escribir cada objeto como una línea en el archivo
            for item in cards:
                writer.writerow(item.values())
        
        print("Archivo 'modo_datos.csv' generado correctamente con los datos de 'cards'.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos: {e}")

if __name__ == "__main__":
    obtener_datos()
