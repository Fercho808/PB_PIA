import requests

API_KEY = "GGzdd1Vm4npty4LFHS5jwWtyYbcdALf67IjpcvEu"

def obtener_datos():
    """Descarga los datos de la API de NASA"""
    
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=2026-05-01&end_date=2026-05-06&api_key={API_KEY}"
    
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    return datos


# IMPRIMIR PARA VER
datos = obtener_datos()
print(datos)
