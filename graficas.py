import procesamiento
import matplotlib.pyplot as plt

lista_nombres = []
lista_tamaño = []
lista_nombres.append(procesamiento.nombre)
lista_tamaño.append(procesamiento.tamaño)

def funcion(lista_nombres, lista_tamaño):
    fig, ax = plt.subplots()
    ax.bar(lista_nombres, lista_tamaño)

    ax.set_title("grafica 1")
    ax.set_ylabel("tamaño")
    ax.set_xlabel("nombre")
    fig.savefig("grafica1.png")
    plt.show()
