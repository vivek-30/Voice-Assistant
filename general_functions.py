from datetime import datetime as dt
from Authentication import user_name
from core_functions import speak,name,take_command,engine
from CLI_Functions import stop_mysql_server
from inquirer import List, prompt
from time import ctime

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

def feedback(feedback):
    if (('good' in feedback) or ('great' in feedback) or ('nice' in feedback) or ('well done' in feedback) or ('i am happy' in feedback) or ('satisfied' in feedback) or ('impressed' in feedback)):
        speak('I am glad that you enjoyed my service sir and i am happy to help you')
        print('Thanks for your appreciation')
    elif (('ok' in feedback) or ('decent' in feedback)):
        speak('glad to help you sir and i will improve myself to provide more accuracy')
        print('Thanks for the valueable feedback')
    elif (('bad' in feedback) or ('worst' in feedback) or ('i am unhappy' in feedback) or ('poor' in feedback) or ('pathetic' in feedback)):
        speak('i am really sorry sir i will update myself to give better performance thanks for the feedback')
        print('Thanks for your valueable feedback,this will help me to improve further')
    return False

def tell_time():
    tell_time = ctime()
    print(tell_time)
    speak(f'current time is {tell_time}')

def tell_name():
    tell_name = f'My name is {name}'
    speak(tell_name)
    print(tell_name)

def get_input_value(total_values = 10):

    question = [ List('value', message='Quantity: ', choices=['1', '5', '10', 'All', 'Custom']) ]
    answer = prompt(question)
    answer = answer['value']
    total = total_values
    if answer == 'Custom':
        total = int(input('Enter value : '))
    elif answer == 'All':
        total = total_values
    else:
        total = int(answer)
    
    return total

def create_file(command):
    file_name = take_command('give file name')

    if 'text' in command or 'simple' in command:
        file_name = file_name+'.txt'
    elif ' dot ' in file_name:
        file_name = file_name.replace(' dot ','.')

    new_file = open(file_name,'w')
    command = take_command(f'would you like to add something your {file_name} file')
    if 'yes' in command or 'hmm' in command or 'ok' in command or 'sure' in command:
        content = take_command('ok sir tell me what to add')
        new_file.write(content)
    new_file.close()

def custom_exit():
    stop_mysql_server() # Stops the msql server before exiting
    print('Sir i am happy to help you , please visit again')
    engine.stop()
    exit()