import matplotlib.pyplot as plt
import api_conexion 
import os 

def grafica1(datos):
    """Gráfica 1: Tamaño de asteroides (barras)"""
    
    nombres = []
    tamaños = []
    
    for fecha, objetos in datos['near_earth_objects'].items(): #Desempaqueta el diccionario y repite fechas y objetos
        for obj in objetos:
            nombres.append(obj['name'])
            tamaño = obj['estimated_diameter']['kilometers']['estimated_diameter_max'] #Accede a 3 diccionarios para saber el tamaño en kilometros
            tamaños.append(tamaño)
    
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(nombres)), tamaños, color='skyblue') #Dibuja la grafica
    plt.xlabel('Número de Asteroide')
    plt.ylabel('Tamaño (km)')
    plt.title('Tamaño de Asteroides')
    plt.savefig('grafica1.png')
    plt.close()


def grafica2(datos):
    """Gráfica 2: Asteroides peligrosos vs no peligrosos (pastel)"""
    
    peligrosos = 0
    no_peligrosos = 0
    
    for fecha, objetos in datos['near_earth_objects'].items():
        for obj in objetos:
            if obj['is_potentially_hazardous_asteroid']: #Aca con el if se usa para separar si son potencialmente peligrosos o no
                peligrosos += 1
            else:
                no_peligrosos += 1
    
    plt.figure(figsize=(8, 6))
    etiquetas = ['Peligrosos', 'No Peligrosos']
    cantidad = [peligrosos, no_peligrosos]
    colores = ['red', 'green']
    plt.pie(cantidad, labels=etiquetas, autopct='%1.1f%%', colors=colores, startangle=90) #Crea la grafica de pastel
    plt.title('Asteroides Peligrosos vs No Peligrosos')
    plt.savefig('grafica2.png')
    plt.close()


def grafica3(datos):
    """Gráfica 3: Velocidad de acercamiento por asteroide (línea)"""
    
    nombres = []
    velocidades = []
    
    for fecha, objetos in datos['near_earth_objects'].items():
        for obj in objetos:
            nombres.append(obj['name'][:15])  
            velocidad = obj['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'] #Acede al primer acercamiento [0] y saca la velocidad en km/h
            velocidades.append(float(velocidad)) #Convierte la velocidad de string a float para poder graficarlo
    
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(nombres)), velocidades, marker='o', color='orange', linewidth=2)
    plt.xlabel('Asteroide')
    plt.ylabel('Velocidad (km/h)')
    plt.title('Velocidad de Acercamiento de Asteroides')
    plt.xticks(range(len(nombres)), nombres, rotation=45, ha='right')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica3.png')
    plt.close()


datos = api_conexion.obtener_datos()
grafica1(datos)
grafica2(datos)
grafica3(datos)
#Los 3 de abajo pues nomas abren las graficas en png
os.startfile('grafica1.png')
os.startfile('grafica2.png')
os.startfile('grafica3.png')
