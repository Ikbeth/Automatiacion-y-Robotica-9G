
# from keras.preprocessing.image import load_img, img_to_array # No sirve despues de 2.9
# from tensorflow.keras.utils import load_img, img_to_array
from keras.utils import load_img, img_to_array

largo, alto = 500, 500 #preferentemente cuadradas o de la misma dimensión, redimencionar + pequeño
file = 'Gato.jpg'

img = load_img(file, target_size=(largo, alto)
               , color_mode="grayscale"
               )

print(img.size)
print(img.mode)

# OPCIÓN 1
# img.show()

# OPCIÓN 2
import matplotlib.pyplot as plt

plt.imshow(img, cmap="gray")
# plt.imshowa(img)
plt.xticks([])
plt.yticks([])
plt.show()

imagen_en_array = img_to_array(img)
# print(imagen_en_array.shape)

# for i in imagen_en_array:
#     print(i)
