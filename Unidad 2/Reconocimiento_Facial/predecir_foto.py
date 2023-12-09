import cv2
from keras.models import load_model
from keras.utils import load_img, img_to_array
import numpy as np

cam = cv2.VideoCapture(0)

alto, largo = 300, 300
modelo = './modelo/modelo.keras'
pesos = './modelo/pesos.keras'

cnn = load_model(modelo)
cnn.load_weights(pesos)

conFotos = 0

while True:
    result, image = cam.read()

    if result:
        cv2.imshow('Camara_Principal', image)

        res = cv2.waitKey(1)  # 1 = NO DETENGO LA EJECUCIÓN
        # print(res, ' ', ord('q'))
        if res == ord('q'):
            cam.release()
            cv2.destroyWindow('Camara_Principal')
            break
        elif res == ord(' '):
            nombre = './Camara/foto_' + str(conFotos) + '.png'
            cv2.imwrite(nombre, image)

            imagen_a_predecir = load_img(nombre, target_size = (alto, largo))
            imagen_a_predecir = img_to_array(imagen_a_predecir)
            imagen_a_predecir = np.expand_dims(imagen_a_predecir, axis=0)  # agrega una dimension adicional
            arreglo = cnn.predict(imagen_a_predecir)  # [[1,0,0,0,0,0]]
            resultado = arreglo[0]
            respuesta = np.argmax(resultado)  # indice del valor mas alto

            match respuesta:
                case 0: print('1-Hafid')
                case 1: print('2-Liz')
                case 2: print('3-Carlos')
                case _: print('----')
            conFotos += 1
        # else:
        #     print('No image detected. Please! try again')
        #     break
