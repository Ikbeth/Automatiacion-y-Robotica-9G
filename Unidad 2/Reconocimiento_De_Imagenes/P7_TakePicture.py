import cv2
cam = cv2.VideoCapture(0)

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
            cv2.imwrite('foto_' + str(conFotos) + '.png', image)
            conFotos += 1
        # else:
        #     print('No image detected. Please! try again')
        #     break
