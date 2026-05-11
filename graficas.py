import matplotlib.pyplot as plt
import api_conexion
import os
def grafica1(datos):
    """Gráfica 1: Tamaño de asteroides""" #barras
    nombres = []
    tamaños = []
    for fecha, objetos in datos['near_earth_objects'].items():
        for obj in objetos:
            nombres.append(obj['name'])
            tamaño = obj['estimated_diameter']['kilometers']['estimated_diameter_max']
            tamaños.append(tamaño)
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(nombres)), tamaños, color='skyblue')
    plt.xlabel('Número de Asteroide')
    plt.ylabel('Tamaño (km)')
    plt.title('Tamaño de Asteroides')
    plt.savefig('grafica1.png')
    plt.close()
def grafica2(datos):
    """Gráfica 2: Asteroides peligrosos vs no peligrosos""" #pastel
    peligrosos = 0
    no_peligrosos = 0
    for fecha, objetos in datos['near_earth_objects'].items():
        for obj in objetos:
            if obj['is_potentially_hazardous_asteroid']:
                peligrosos += 1
            else:
                no_peligrosos += 1
    plt.figure(figsize=(8, 6))
    etiquetas = ['Peligrosos', 'No Peligrosos']
    cantidad = [peligrosos, no_peligrosos]
    colores = ['red', 'green']
    plt.pie(cantidad, labels=etiquetas, autopct='%1.1f%%', colors=colores, startangle=90)
    plt.title('Asteroides Peligrosos vs No Peligrosos')
    plt.savefig('grafica2.png')
    plt.close()
datos = api_conexion.obtener_datos()
grafica1(datos)
grafica2(datos)
os.startfile('grafica1.png')
os.startfile('grafica2.png')
