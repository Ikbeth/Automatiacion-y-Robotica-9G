
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

arduino = serial.Serial('COM8', 9600, timeout=1)


def reconocer(cadena):
    # avanzar = ['avanza', 'avanzar', 'avancen', 'avanza', 'avanzas', 'avanzan', 'avanza', 'avanzalo', 'Avanza', 'Avanzar',
    #            'Avancen', 'Avanza', 'Avanzas', 'Avanzan', 'Avanza', 'Avanzalo']
    go = ['go', 'Go', 'GO', 'forward', 'Forward', 'FORWARD', 'ahead', 'Ahead', 'AHEAD']
    # retroceder = ['retrocede', 'retroceder', 'retrocedan', 'retrocede', 'retrocedes', 'retroceden', 'retrocede',
    #               'retrocedelo', 'Retrocede', 'Retroceder', 'Retrocedan', 'Retrocede', 'Retrocedes', 'Retroceden',
    #               'Retrocede', 'Retrocedelo', 'atras']
    back = ['back', 'Back', 'BACK', 'backward', 'Backward', 'BACKWARD', 'backwards', 'Backwards', 'BACKWARDS']
    # derecha = ['derecha', 'derecho', 'derechan', 'derecha', 'derechas', 'derechan', 'derecha', 'derechalo', 'Derecha',
    #            'Derecho', 'Derechan', 'Derecha', 'Derechas', 'Derechan', 'Derecha', 'Derechalo']
    right = ['right', 'Right', 'RIGHT']
    # izquierda = ['izquierda', 'izquierdo', 'izquierdan', 'izquierda', 'izquierdas', 'izquierdan', 'izquierda',
    #              'izquierdalo', 'Izquierda', 'Izquierdo', 'Izquierdan', 'Izquierda', 'Izquierdas', 'Izquierdan',
    #              'Izquierda', 'Izquierdalo']
    left = ['left', 'Left', 'LEFT']
    # detener = ['detente', 'detener', 'detenganse', 'detente', 'detentes', 'detengansen', 'detente', 'detenlo', 'Detente',
    #            'Detener', 'Detenganse', 'Detente', 'Detentes', 'Detengansen', 'Detente', 'Detenlo', 'para', 'alto']
    stop = ['stop', 'Stop', 'STOP']

    for i in go:
        if i in cadena:
            return '0'
    for i in back:
        if i in cadena:
            return '1'
    for i in right:
        if i in cadena:
            return '2'
    for i in left:
        if i in cadena:
            return '3'
    for i in stop:
        if i in cadena:
            return '4'
    return ''


def grabar():
    with m as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Registro Generado!:")

    try:
        cadena = r.recognize_google(audio, language="en-US")  # en-US, es-MX
        print("Menaje: " + cadena)

        cad_arduino = reconocer(cadena)

        # ENVIAR CADENA A ARDUINO
        if not cad_arduino == '':  # probar
            if not arduino is None:
                arduino.write(cad_arduino.encode())
                print("Cadena enviada a Arduino: ", cad_arduino)

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

# semana 9 de 16
# tema 3.6 rutinas y tareas de control / unidad robóticca móvil