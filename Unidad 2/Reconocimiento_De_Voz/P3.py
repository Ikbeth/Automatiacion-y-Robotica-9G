import speech_recognition as sr
r=sr.Recognizer()
print("inicia:")
audio_file=sr.AudioFile('Audio/audio_fie_1.wav')

try:
    with audio_file as source:
        audio=r.record(source)
    var= r.recognize_google(audio,language="es-MX", show_all=True)
    print("Menaje: ")
    print(var)


except sr.UnknownValueError as e:
    print("Unknown Value Error",e)
except sr.RequestError as e:
    print("Request Error: ".format(e))
except Exception as ex:
    print("Error: ".format(ex))
