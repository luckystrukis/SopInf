import cv2

clasificador_de_rostros = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#foto_prueba_1.jpg
#foto_rostros_0.jpg
image = cv2.imread('fotos/foto_rostros_0.jpg')
copia_imagen = image.copy()
rostro = clasificador_de_rostros.detectMultiScale(image)
if not rostro.all():
    print("no hay cara")
else:
    print(rostro)
for (x,y,anch,alto) in rostro:
    cv2.rectangle(image,(x,y),(rostro[0]+rostro[2],rostro[1]+rostro[3],0,255,255),2)
    rostro = copia_imagen[y:rostro[1]+rostro[3],x:rostro[0]+rostro[2]]
    cv2.imwrite(rostro.jpg, rostro)