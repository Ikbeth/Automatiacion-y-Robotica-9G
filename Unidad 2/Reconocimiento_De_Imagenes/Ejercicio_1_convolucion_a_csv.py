
from keras.utils import load_img, img_to_array, array_to_img

nombre = 'L_15'
largo, alto = 250, 250
file = nombre + '.jpeg'
nombre_csv = './CSV/csv_' + nombre + '.csv'

img = load_img(file, target_size=(largo, alto)
               , color_mode="grayscale"
               )

img_a_convolucionar = img_to_array(img)

kernel = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

img_convolucionada = []
archivo_imagen = open(nombre_csv, 'w')

for filas in range(1, alto-1):
    new_fila = []
    for columnas in range(1, largo-1):
        pixelConvolucionado = 0
        for f_kernel in range(len(kernel)):
            for c_kernel in range(len(kernel)):
                pixelConvolucionado += (kernel[f_kernel][c_kernel]
                                        * img_a_convolucionar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)])
        pixelConvolucionado = pixelConvolucionado / 9
        pixel = str(pixelConvolucionado).replace('[','').replace(']','') + ","
        archivo_imagen.write(pixel)
        new_fila.append(pixelConvolucionado)
    img_convolucionada.append(new_fila)
    archivo_imagen.write("\n")
archivo_imagen.flush()
archivo_imagen.close()

newImage = array_to_img(img_convolucionada)
print(newImage.size)

import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))

plt.subplot(1,2,1)
plt.xticks([])
plt.yticks([])
plt.imshow(img, cmap='gray')

plt.subplot(1,2,2)
plt.xticks([])
plt.yticks([])
plt.imshow(newImage, cmap='gray')

plt.show()
