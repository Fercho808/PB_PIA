import procesamiento
import api_conexion
import graficas
datos = api_conexion.obtener_datos()
resultado = procesamiento.procesar(datos)
print (resultado)
