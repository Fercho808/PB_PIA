import procesamiento
import api_conexion
datos = api_conexion.obtener_datos()
resultado = procesamiento.procesar(datos)
print (resultado)
