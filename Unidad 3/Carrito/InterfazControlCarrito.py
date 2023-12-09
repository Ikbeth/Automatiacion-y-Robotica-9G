
import tkinter as tk
import customtkinter

import serial

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("700x400")

arduino = None


def conecta():
    global arduino
    if button_connect.cget("text") == "CONECTAR":
        arduino = serial.Serial('COM8', 9600, timeout=0)
        button_connect.configure(text="DESCONECTAR")
        print('conectado')
    elif button_connect.cget("text") == "DESCONECTAR":
        arduino.close()
        button_connect.configure(text="RECONECTAR")
        print('desconectado')
    else:
        arduino.open()
        button_connect.configure(text="DESCONECTAR")
        print('conectado')


def mover(num):
    if not arduino is None:
        arduino.write(str(num).encode())
        print("Cadena enviada a Arduino: ", num)


title = customtkinter.CTkLabel(master=app, width=500, height=150)
title.configure(text='CONTROL CARRITO', text_color='white', font=('arial', 36))
title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_front = customtkinter.CTkButton(master=app, width=200, height=60, command=lambda: mover(0))
button_back = customtkinter.CTkButton(master=app, width=200, height=60, command=lambda: mover(1))
button_left = customtkinter.CTkButton(master=app, width=200, height=60, command=lambda: mover(3))
button_right = customtkinter.CTkButton(master=app, width=200, height=60, command=lambda: mover(2))
button_stop = customtkinter.CTkButton(master=app, width=200, height=60, command=lambda: mover(4))
button_connect = customtkinter.CTkButton(master=app, width=200, height=60, command=conecta)

app.bind("<Up>", lambda event: mover(0))
app.bind("<w>", lambda event: mover(0))
app.bind("<Down>", lambda event: mover(1))
app.bind("<s>", lambda event: mover(1))
app.bind("<Left>", lambda event: mover(3))
app.bind("<a>", lambda event: mover(3))
app.bind("<Right>", lambda event: mover(2))
app.bind("<d>", lambda event: mover(2))
app.bind("<space>", lambda event: mover(4))


button_front.configure(text="FRENTE")
button_back.configure(text="RETROCEDER")
button_left.configure(text="IZQUIERDA")
button_right.configure(text="DERECHA")
button_stop.configure(text="DETENER")
button_connect.configure(text="CONECTAR")

button_front.place(relx=0.5, rely=0.32, anchor=tk.CENTER)
button_back.place(relx=0.5, rely=0.68, anchor=tk.CENTER)
button_left.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
button_right.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
button_stop.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
button_connect.place(relx=0.16, rely=0.9, anchor=tk.CENTER)

app.mainloop()
