
import tkinter as tk
import customtkinter

import threading

import speech_recognition as sr

import serial

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("300x150")

r = sr.Recognizer()
m = sr.Microphone()

arduino = serial.Serial('COM3', 9600, timeout=1)


def encender(cadena):
    encender = ['enciende', 'encender', 'enciendan', 'enciende', 'enciendes', 'encienden', 'encienda', 'enciendalo',
                'Enciende', 'Encender', 'Enciendan', 'Enciende', 'Enciendes', 'Encienden', 'Encienda', 'Enciendalo']
    accion_encender = 0
    for i in encender:
        if i in cadena:
            accion_encender = 1
            break
    return accion_encender


def apagar(cadena):
    apagar = ['apaga', 'apagar', 'apagan', 'apaga', 'apagas', 'apagan', 'apaga', 'apagalo', 'Apaga', 'Apagar', 'Apagan',
              'Apaga', 'Apagas', 'Apagan', 'Apaga', 'Apagalo']
    accion_apagar = 0
    for i in apagar:
        if i in cadena:
            accion_apagar = 1
            break
    return accion_apagar


def reconocer(cadena):
    lugar = ['sala', 'recámara', 'baño']

    accion_encender = encender(cadena)
    accion_apagar = apagar(cadena)

    if 'foco' in cadena:
        foco = 1
    else:
        foco = 0

    if 'estéreo' in cadena:
        estereo = 1
    else:
        estereo = 0

    if 'televisión' in cadena or 'televisor' in cadena:
        television = 1
    else:
        television = 0

    if lugar[0] in cadena:
        lugar = 1
    elif lugar[1] in cadena:
        lugar = 2
    elif lugar[2] in cadena:
        lugar = 3
    else:
        lugar = 0

    if accion_encender == 0 and accion_apagar == 0:
        print("No se reconoce el comando")
        cad_arduino = '0'
    else:
        print("Comando reconocido")
        cad_arduino = (str(foco) + str(estereo) + str(television) + str(accion_encender) + str(accion_apagar)
                       + str(lugar))
        # print("Cadena a enviar: foco, estéreo, televisión, encender, apagar, lugar")
        # print(cad_arduino)

    return cad_arduino


def grabar():
    with m as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Registro Generado!:")
    with open("Audio/audio_arduino", "wb") as file:
        file.write(audio.get_wav_data())
    # print("Archivo Creado!")

    try:
        cadena = r.recognize_google(audio, language="es-MX")
        print("Menaje: " + cadena)

        cad_arduino = reconocer(cadena)

        # ENVIAR CADENA A ARDUINO
        # arduino.open()
        if not cad_arduino == '0':  # probar
            if not arduino is None:
                arduino.write(cad_arduino.encode())
                # arduino.close()
                print("Cadena enviada a Arduino")

    except sr.UnknownValueError:
        print("Unknown Value Error")
    except sr.RequestError as e:
        print("Request Error: ".format(e))
    except Exception as ex:
        print("Error: ".format(ex))

    button_record.configure(text="Grabar")


def record():
    if button_record.cget("text") == "Grabar":
        button_record.configure(text="Grabando")
        threading.Thread(target=grabar).start()


button_record = customtkinter.CTkButton(master=app, width=200, height=60, command=lambda: record())
button_record.configure(text="Grabar")
button_record.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

app.mainloop()
