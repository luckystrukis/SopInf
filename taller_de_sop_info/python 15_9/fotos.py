import cv2
from numpy import array
import pandas as pd

clasificador_de_rostros = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
for i in range(101):
    image = cv2.imread('fotos/foto_rostros_' + str(i) + '.jpg')
    copia_imagen = image.copy()
    rostro = array(clasificador_de_rostros.detectMultiScale(image))
    ROSTROS = 0
    for (x, y, ancho, alto) in rostro:
        cv2.rectangle(image, (x, y), (x+ancho, y+alto), (0, 255, 255), 2)
        rostro = copia_imagen[y:y+alto, x:x+ancho]
        cv2.imwrite('fotosrecortadas/rostro' + str(i) + '.jpg', rostro)
        ROSTROS = ROSTROS + 1
    if i == 0:
        diccionario = {'nombre': "foto_rostros_" +
                       str(i), 'numero rostros': str(ROSTROS)}
        dataframecant = pd.DataFrame(
            diccionario, columns=['nombre', 'numero rostros'], index=[i])
    else:
        diccionario = {'nombre': "foto_rostros_" +
                       str(i), 'numero rostros': str(ROSTROS)}
        dataframe2cant = pd.DataFrame(
            diccionario, columns=['nombre', 'numero rostros'], index=[i])
        dataframecant = pd.concat([dataframecant, dataframe2cant])
    if i == 0:
        diccionario = {'nombre': "foto_rostros_" +
                       str(i) + ".jpg", 'posicion x': str(x), 'posicion y': str(y)}
        dataframe = pd.DataFrame(diccionario, columns=[
                                 'nombre', 'posicion x', 'posicion y'], index=[i])
    else:
        diccionario = {'nombre': "foto_rostros_" +
                       str(i) + ".jpg", 'posicion x': str(x), 'posicion y': str(y)}
        dataframe2 = pd.DataFrame(diccionario, columns=[
                                  'index', 'nombre', 'posicion x', 'posicion y'], index=[i])
        dataframe = pd.concat([dataframe, dataframe2])

print(dataframe)
dataframe.index.name = 'id'
dataframe.to_csv("fotos.csv")
dataframecant.to_csv("fotoscant.csv")
