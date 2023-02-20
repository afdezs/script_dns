# Propiedad de Adrian Fdz.

#Importamos las librerías necesarias:
import urllib.request #Proporciona recursos de Internet por URLs
import os #Proporciona acceder a funciones dependientes del Sistema Operativo

APIKey='curl -X GET ">> Aquí se incluye la URL de la API de IONOS <<"'

#Creamos la variable IP_actual para consultar la IP pública que tenemos:
IP_actual=urllib.request.urlopen('https://ident.me').read().decode('utf8')
#Con el print mostramos la IP Actual:
print(IP_actual)

#Creamos la variable IP_antigua para consultar el archivo donde tenemos la IP almacenada, accediento en modo lectura:
IP_antigua=file=open("antigua_IP.txt","r").readline(20)
#Con el print mostramos la IP Antigua:
print(IP_antigua)

#Creamos las condiciones:
if IP_actual==IP_antigua:
    print ("No ha cambiado la IP pública.")
else:
#Abrimos el archivo antigua_IP en modo escritura y escribimos la IP Actual:
    file=open("antigua_IP.txt", "w")    
    file.write(IP_actual)
    file.close()
#Cerramos el archivo y hacemos print mostrando que se han realizado los cambios:
    print ("La IP pública ha sido cambiada con éxito.")
#Con esto actualizamos en IONOS la nueva IP pública con la API para que se haga efectivo el cambio en la configuración DNS:
#(Este comando posee de forma encriptada las credenciales de acceso a la API de IONOS propias de nuestro dominio):
    os.system (APIKey)