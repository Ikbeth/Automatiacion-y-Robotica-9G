import speech_recognition as sr
r=sr.Recognizer()
print("inicia:")
with sr.Microphone() as source:
#r.adjust_for_ambient_noise(source)#listen 4 1 sec
#to calibrate the energy threshold for ambient noise levels
    audio=r.listen(source)

    print("Registro Generado!:")

try:
    #print("Menaje: "+ r.recognize_google(audio))
    cadena= r.recognize_google(audio,language="es-MX")
    print("Menaje: "+ cadena)
except sr.UnknownValueError:
    print("Unknown Value Error")
except sr.RequestError as e:
    print("Request Error: ".format(e))
except Exception as ex:
    print("Error: ".format(ex))
