import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[7].id)
r = sr.Recognizer()

name = 'jarvis'

def speak(order):
    engine.say(order)
    engine.runAndWait()

def take_command(ask = False):
    print('wait for 2 sec and then speak') 
    if ask:
        speak(ask)
    with sr.Microphone() as source:
        # audio = r.adjust_for_ambient_noise(source,duration = 1)
        audio = r.listen(source)
        command = ''
        try:
           command = r.recognize_google(audio)
           print('Done with voice input')
           command = command.lower()
        except sr.UnknownValueError:
            speak('sir please speak again')
        except sr.RequestError:
            speak('sir either you are not connected to internet or there is something wrong with your microphone please try after some time')
        return command
