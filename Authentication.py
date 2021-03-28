import mysql.connector
from time import sleep
from subprocess import call
from sys import platform
from CLI_Functions import start_mysql_server
from core_functions import speak,take_command
from inquirer import List, prompt
from getpass import getpass

start_mysql_server()

mydbs = mysql.connector.connect(host = "localhost",user = "root",passwd = "",db = "jarvis_users")
mycursor = mydbs.cursor(buffered = True)

user_name = ''

def take_user_name(string = ''):
    global user_name
    if string == '':
        string = 'please tell me your name'
    user_name = take_command(string)
    if 'my name is' in user_name:
        user_name = user_name.replace('my name is ','')
    elif 'i am' in user_name:
        user_name = user_name.replace('i am ','')

def add_new_user(password,gender):

    global user_name
    if user_name == '':
        speak('sorry sir i am unable to grab your name please try again later')
        print('Empty name are not allowed')
        return '501'

    print('Joining ...')
    speak('please wait a momment we are joining you to our community')

    mycursor.execute('SELECT * FROM users LIMIT 1')
    result = mycursor.fetchone()
    if result:
        search_query = f'SELECT * FROM users WHERE name=\"{user_name}\"'           
        mycursor.execute(search_query)
        result = mycursor.fetchone()

        if gender == 'Male':
            gen = 'sir'
        else:
            gen = 'mam'

        if result:
            print('username is already taken')
            speak(f'{gen} please choose a different username')
            return '405'

        search_query = f'SELECT * FROM users WHERE password=\"{password}\"'           
        mycursor.execute(search_query)
        result = mycursor.fetchone()
        if result:
            print('password is already taken')
            speak(f'{gen} please choose a different password')
            return '405'
        
    add_query = f'INSERT INTO users (name,password,gender) VALUES (\"{user_name}\",\"{password}\",\"{gender[0]}\")'
    mycursor.execute(add_query)
    mydbs.commit()
    
    search_query = f'SELECT * FROM users WHERE name=\"{user_name}\" and password=\"{password}\"'
    mycursor.execute(search_query)
    result = mycursor.fetchone()

    if result:
        print(f'{mycursor.rowcount} new user added with name = \"{user_name}\"')
        speak('you have successfully joined welcome to jarvis community')
        print('Thanks for joining')
        return '200'
    else:
        speak('there is something wrong with our backend we will fix it soon')
        speak('sorry for inconvenience sir')
        return '503'

def verify_user(password):

    global user_name
    if password == '':
       take_user_name('sir you did not enter the password tell me your name')
       mycursor.execute(f'SELECT admin FROM users WHERE name = \"{user_name}\"')
       result = mycursor.fetchone()
       if result and 'Yes' in result:
            speak('you are logged in as a super user welcome')
            return '200'
       else:
            speak('sir you are not a super user so you cant use this service')
            return '405'
    else:
        print('verifying ...')
        speak('please wait a momment we are connecting you')
        mycursor.execute('SELECT * FROM users LIMIT 1')
        result = mycursor.fetchall()
        if result:
            verify_query = f'SELECT * FROM users WHERE name=\"{user_name}\" AND password=\"{password}\"'
            mycursor.execute(verify_query)
            result = mycursor.fetchone()
            if result:
                print('Enjoy The Service.')
                speak('connected successfully')
                return '200'
            else:
                print('No user found ,may be because of wrong user name or password')
                speak('sir i think you are not a existing user or there is something wrong please try again after some time')
                print('Try again later.')
                return '405'

def authenticate():
    response = '405'
    global user_name
    command = take_command('sir are you a new user or existing one')

    if (('new' in command) and ('exiting' in command)):
        speak('sorry sir i am unable to sir serve you')

    elif 'existing' in command or 'not new' in command or 'now a new' in command or 'old' in command:
        speak('ok sir provide your username or password to use this service') 
        take_user_name()
        if user_name.strip() != '':
            speak('Enter your Password')
            password = getpass(prompt='Password: ').strip()
            response =  verify_user(password)

    elif 'new' in command:
        speak('ok sir welcome to my service i will need your details to use this service') 
        take_user_name()
        speak('tell me your gender')
        question = [ List('gender', message="Your Gender: ", choices=[ 'Male', 'Female' ]) ]
        answer = prompt(question) 
        speak('set a password')
        password = getpass(prompt='Password: ').strip()
        response = add_new_user(password, answer['gender'])
    
    return response

def initiate():
    speak('sir before i start make sure you have a decent internet connection.')
    input('Hit Enter To Proceed')
    return authenticate()