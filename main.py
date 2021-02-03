import pyttsx3
import speech_recognition as sr
from time import ctime

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

    elif 'time' in command:
        tell_time = ctime()
        print(tell_time)
        speak(f'current time is {tell_time}')
        
    elif 'create' in command and 'file' in command:

        file_name = take_command('give file name')

        if 'text' in command or 'simple' in command:
            file_name = file_name+'.txt'
    
        elif ' dot ' in file_name:
            file_name = file_name.replace(' dot ','.')
        new_file = open(file_name,'w')
        command = take_command(f'would you like to add something your {new_file} file')
        if command in "yes ok yaah yup hmmm y":
            content = take_command('ok sir tell me what to add')
            new_file.write(content)
        new_file.close()

if __name__ == '__main__':
    while True:
        command = take_command('how may i help you')
        print(f'you said : {command}')
        execute_command(command)