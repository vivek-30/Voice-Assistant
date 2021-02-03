import pyttsx3
import speech_recognition as sr

name = 'jarvis'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[7].id)
r = sr.Recognizer()

def speak(order):
    engine.say(order)
    engine.runAndWait()

def take_command(ask = False):
    if ask:
        speak(ask)
    with sr.Microphone() as source:
        # audio = r.adjust_for_ambient_noise(source,duration = 1)
        audio = r.listen(source)
        command = ''
        try:
           print('speak ...') 
           command = r.recognize_google(audio)
           print('Done with voice input')
           command = command.lower()
        except sr.UnknownValueError:
            speak('sir please speak again')
        except sr.RequestError:
            speak('sir either you are not connected to internet or there is something wrong with your microphone please try after some time')
        return command

def execute_command(command):
    if 'name' in command:
        tell_name = f'My name is {name}'
        speak(tell_name)
        print(tell_name)

    elif 'exit' in command or 'quit' in command:
        engine.stop()
        exit()

if __name__ == '__main__':
    while True:
        command = take_command('how may i help you')
        print(f'you said : {command}')
        execute_command(command)