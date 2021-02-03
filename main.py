import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
from datetime import datetime as dt
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

def greet():
    global user_name
    hour = int(dt.now().hour)

    if user_name == '':
        user_name = 'sir'

    if hour>0 and hour<12:
        day_span = 'Morning'
    elif hour>=12 and hour<17:
        day_span = 'Afternoon'
    elif hour>=17 and hour<20:
        day_span = 'Evening'
    else:
        day_span = 'Night'
    speak(f'Good {day_span} {user_name} how can I help you')

def manage_search(query):

    if len(query) == 0:
        return
    
    if 'search' in query:
        query = query.replace('search','')
    elif 'find' in query:
        query = query.replace('find','')
    elif 'show' in query:
        query = query.replace('show','')
    elif 'show me some' in query:
        query = query.replace('show me some','')
    elif 'show me' in query:
        query = query.replace('show me','')
    elif 'show some' in query:
        query = query.replace('show some','')
    elif 'display' in query:
        query = query.replace('display','')
    elif 'display me some' in query:
        query = query.replace('display me some','')
    elif 'display some' in query:
        query = query.replace('display','')
    elif 'display me' in query:
        query = query.replace('display me','')

    if 'in google' in query:
        query = query.replace('in google','')
    elif 'on google' in query:
        query = query.replace('on google','')
    elif 'in youtube' in query:
        query = query.replace('in youtube','')
    elif 'on youtube' in query:
        query = query.replace('on youtube','')
    
    query = query.split('for')[-1]

    return query.strip()

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

        elif (('search' in command  or 'find' in command or 'display' in command or 'show' in command) and ('youtube' not in command)):
        search_item = manage_search(command)
        if search_item:
            url = f"https://google.com/search?q={search_item}"
            webbrowser.get().open(url)
            speak('these are the results for '+search_item+' on google')
        else:
            speak('empty search is redundant')

    elif (('search' in command or 'find' in command or 'display' in command or 'show' in command) and ('youtube' in command)):
        search_item = manage_search(command)
        if search_item:
            url = f"https://youtube.com/results?search_query={search_item}"
            webbrowser.get().open(url)
            speak('these are the results for '+search_item+' on youtube')
        else:
            speak('empty search is redundant')
            
    elif 'wikipedia' in command or 'wiki' in command:
        command = command.replace('wikipedia','')
        speak('how many lines do you want in your results')
        lines = int(input('=> '))

        if lines <= 0:
            speak('provide a feasible number')
        elif lines > 10:
            speak('this is too much data this permission is not allowed by vivek')
        else:
            results = wikipedia.summary(command,sentences = lines)
            speak('here is what all i have found regarding '+command)
            print(results)
            speak(results)

if __name__ == '__main__':
    while True:
        command = take_command('how may i help you')
        print(f'you said : {command}')
        execute_command(command)