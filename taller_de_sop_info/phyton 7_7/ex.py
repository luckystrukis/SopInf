import cv2

clasificador_de_rostros = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

image = cv2.imread('fotos/52f40c59-7839-4711-9b6c-a8fbcfa750b5.jpeg')
copia_imagen = image.copy()
rostros = clasificador_de_rostros.detectMultiScale(image)

i = 0
for (x, y, ancho, alto) in rostros:
    cv2.rectangle(image, (x, y), (x+ancho, y+alto),(0, 255, 255), 2)
    rostro = copia_imagen[y:y+alto,x:x+ancho]
    print("Hay un rostro")
    cv2.imwrite('rostro' + str(i) + '.jpg', rostro)
    i = i+1