import cv2
import threading
from datetime import datetime

cam = cv2.VideoCapture(0)

ruta = './Entrenamiento/1-Hafid/'
# ruta = './Entrenamiento/2-Liz/'
# ruta = './Entrenamiento/3-Carlos/'
conFotos = 0


def tomar_fotos():
    for i in range(50):
        fecha = datetime.now()
        fecha = fecha.strftime('%d_%m_%Y_%H_%M_%S_%f')
        nombre = ruta + 'foto_' + fecha + '.png'
        cv2.imwrite(nombre, image)
    print('Listo')


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
            threading.Thread(target=tomar_fotos).start()
        # else:
        #     print('No image detected. Please! try again')
        #     break
