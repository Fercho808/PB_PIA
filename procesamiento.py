import requests

API_KEY = "GGzdd1Vm4npty4LFHS5jwWtyYbcdALf67IjpcvEu"

def procesar(datos):
    
    lista_limpia = []
    
    for fecha, objetos in datos['near_earth_objects'].items():
        for obj in objetos:
            nombre = obj['name']
            tamaño = obj['estimated_diameter']['kilometers']['estimated_diameter_max']
            peligroso = obj['is_potentially_hazardous_asteroid']
            
            lista_limpia.append({
                'nombre': nombre,
                'tamaño': tamaño,
                'peligroso': peligroso
            })
    
    return lista_limpia

url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=2026-05-01&end_date=2026-05-06&api_key={API_KEY}"
respuesta = requests.get(url)
datos = respuesta.json()

resultado = procesar(datos)

for item in resultado:
    print(item)

print(f"\nTotal: {len(resultado)} asteroides")
