
from keras.utils import load_img, img_to_array

largo, alto = 250, 250
file = 'Gato.jpg'

img = load_img(file, target_size=(largo, alto)
               , color_mode="grayscale"
               )

print(img.size)
print(img.mode)

imagen_en_array = img_to_array(img)

for filas in range(1, alto-1):
    # print('Fila: ', filas + 1, end=' ')
    for columnas in range(1, largo-1):
        print(imagen_en_array[filas][columnas][0], end=' ')
    print('')
