from keras.utils import load_img, img_to_array, array_to_img, save_img
import matplotlib.pyplot as plt
import os
import shutil


def getArrayImage(nombre_archivo, largo, alto):
    img_original = load_img(nombre_archivo, target_size=(largo, alto), color_mode='grayscale')
    img_en_arreglo = img_to_array(img_original)
    # print(img_en_arreglo.shape)
    return img_en_arreglo


def maxPooling(stride, img_array, largo, alto):
    img_max_pooling = []
    for filas in range(1, alto - 1, stride):
        new_fila = []
        for columnas in range(1, largo - 1, stride):
            max_pixel = -1
            for f_kernel in range(stride):
                for c_kernel in range(stride):
                    pixel = img_array[filas + f_kernel][columnas + c_kernel]
                    if pixel > max_pixel:
                        max_pixel = pixel
            new_fila.append(float(max_pixel))
        img_max_pooling.append(new_fila)

    return img_max_pooling


def convolucionar(img_a_convolucinar, kernel_type, largo, alto):
    break_convolution = 1
    match kernel_type:
        case "0": # IDENTITY
            kernel = [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ]
            div = 1
            break_convolution = 0
        case "1": # RIDGE 1
            kernel = [
                [0, -1, 0],
                [-1, 4, -1],
                [0, -1, 0]
            ]
            div = 1
            break_convolution = 0
        case "2":  # RIDGE 2
            kernel = [
                [-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]
            ]
            div = 1
            break_convolution = 0
        case "3":  # SHARPEN
            kernel = [
                [0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0]
            ]
            div = 1
            break_convolution = 0
        case "4":  # BOX BLUR
            kernel = [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ]
            div = 9
            break_convolution = 0
        case "5":  # GAUSSIAN BLUR
            kernel = [
                [1, 2, 1],
                [2, 4, 2],
                [1, 2, 1]
            ]
            div = 16
            break_convolution = 0
        case _:
            print("kernel no valido")
            break_convolution = 1

    if not break_convolution:
        img_convolucionada = []
        for filas in range(1, alto - 1):
            new_fila = []
            for columnas in range(1, largo - 1):

                pixelConvulucionado = 0
                for f_kernel in range(len(kernel)):
                    for c_kernel in range(len(kernel)):
                        pixelConvulucionado += kernel[f_kernel][c_kernel] \
                                               * img_a_convolucinar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)]
                pixelConvulucionado = pixelConvulucionado / div
                new_fila.append(pixelConvulucionado)
            img_convolucionada.append(new_fila)
        return img_convolucionada
    else:
        return None


def plotImages(imgOrginal, imgConvolucionada):
    # plot - 2 imagenes
    plt.figure(figsize=(5, 5))

    plt.subplot(1, 2, 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(array_to_img(imgOrginal), cmap='gray')

    plt.subplot(1, 2, 2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(imgConvolucionada, cmap='gray')

    plt.show()


def get_folders_name_from(from_location, ignored_directories):
    list_dir = os.listdir(from_location)
    folders = []
    for file in list_dir:
        temp = os.path.splitext(file)
        if temp[1] == "" and (temp not in ignored_directories):
            folders.append(temp[0])
    return folders


# kernel 1
def filtro1(imagen_a_convolucionar):
    return imagen_a_convolucionar


base_location = "./"
source_folder = 'ImagenesPersonales'  # CREAR CARPETAS MANUALMENTE PARA QU FUNCIONE
destination_folder = 'CreaCarpetas'  # SE PUEDEN MODIFICAR
ignored_directories = ['.idea', '.DS_Store']  # or other folders

name_folders = get_folders_name_from(base_location + source_folder, ignored_directories)  # custom location
# print(name_folders)

for folder in name_folders:
    try:
        # read content - source location
        rutaImagen = base_location + source_folder + "/" + folder
        imgs = [archivo for archivo in os.listdir(rutaImagen) if archivo.endswith(".jpeg")]

        # write content - destination location
        exists = os.path.exists(base_location + destination_folder + '/' + folder)
        if exists:
            shutil.rmtree(base_location + destination_folder + '/' + folder)  # remove folder and subfolders

        # create a new folder...
        os.mkdir(base_location + destination_folder + '/' + folder)

        for k in range(6):  # tot_kernels
            ruta = base_location + destination_folder + '/' + folder + "/Kernel_" + str(k)
            os.mkdir(ruta)
            print('kernel ', str(k))
            for imagen in imgs:
                rutaImagenActual = rutaImagen + "/" + imagen
                # REGRESA IMAGEN EN ARRAY
                img_a_procesar = getArrayImage(rutaImagenActual, 500, 500)
                print(imagen)
                kernel = str(k)
                img_convolucionada = convolucionar(img_a_procesar, kernel, 500, 500)
                # img = array_to_img(img_convolucionada)
                # GUARDA IMG
                rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conFiltro_" + str(k) + ".jpeg"
                save_img(rutaToSave, img_convolucionada)
                # DEFINIR STRIDE 2 x 2
                stride = 2
                img_convolucionada = maxPooling(stride, img_convolucionada, 497, 497)
                # img = array_to_img(img_convolucionada)
                # GUARDA IMG
                rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conMaxPooling_" + str(k) + ".jpeg"
                save_img(rutaToSave, img_to_array(img_convolucionada))
                #######################################################################################################

    except Exception as ex:
        print('-----> ERROR!!!   ', ex)
    finally:
        pass
