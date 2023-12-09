
from keras.utils import load_img, img_to_array, array_to_img


def getArrayImage(nombre_archivo, largo, alto):
    img_original = load_img(nombre_archivo, target_size= (largo, alto), color_mode= 'grayscale')
    img_en_arreglo = img_to_array(img_original)
    return img_en_arreglo


largo, alto = 500, 500

file = './Liz/LatofskiMoreno_12.jpeg'

img_array = getArrayImage(file, largo, alto)
print(img_array.shape)

stride = 3  # 2 x 2

img_max_pooling = []
for filas in range(1, alto - 1,stride):
    new_fila = []
    for columnas in range(1,largo - 1, stride):
        max_pixel = -1
        for f_kernel in range(stride):
            for c_kernel in range(stride):
                pixel =img_array[filas + f_kernel][columnas + c_kernel]
                if pixel > max_pixel:
                    max_pixel = pixel
        new_fila.append(max_pixel)
    img_max_pooling.append(new_fila)

img = array_to_img(img_max_pooling)
print(img.size)
img.show()
