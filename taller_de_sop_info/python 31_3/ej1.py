import requests
import time

if __name__ == '__main__':

    archivo = open("hola.csv", "w")
    nombres_columnas = "mensaje , status \n"
    archivo.write(nombres_columnas)
    archivo.close()
    

    for i in range(100):
        respuesta = requests.get('https://api.jikan.moe/v4/anime/20/episodes/random')
        respuesta.status_code
        informacion = respuesta.json()
        mensaje = informacion["message"]

        linea = mensaje + ","  + "\n"

        archivo = open("hola1.csv", "a")
        archivo.write(linea)
        archivo.close()
        time.sleep(0.5)