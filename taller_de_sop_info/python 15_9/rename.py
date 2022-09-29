import os
for i in range(102):
    if i == 101:
        os.rename('fotos/' + str(i) + '.jpg', 'fotos/foto_rostros_' + str(i) + '.jpg')
    else:
        print("pinto")