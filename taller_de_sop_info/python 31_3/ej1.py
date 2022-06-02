import requests


if __name__ == '__main__':

    archivo = open("hola.csv", "w")
    nombres_columnas = "mensaje , status \n"
    archivo.write(nombres_columnas)
    archivo.close()
    
    for i in range(10):
        respuesta = requests.get('https://dog.ceo/api/breeds/image/random')
        respuesta.status_code
        informacion = respuesta.json()
        mensaje = informacion["message"]
        estado = informacion["status"]

        linea = mensaje + "," + estado + "\n"

        archivo = open("hola.csv", "a")
        archivo.write(linea)
        archivo.close()