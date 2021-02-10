from core_functions import speak,take_command,name
from Authentication import authenticate,user_name,initiate
from CLI_Functions import *
from general_functions import *
from search_fucntions import search,get_wiki
from More_Features import get_news_feeds,capture_image,manage_image
from time import ctime

def execute_command(command):
    if 'name' in command:
        tell_name()

    elif (('up time' in command) or ('mac' in command and 'time' in command)):
        uptime()

    elif 'exit' in command or 'quit' in command:
        custom_exit()

    elif 'time' in command:
        tell_time()
        
    elif 'create' in command and 'file' in command:
        create_file(command)

    elif (('capture' in command or 'click' in command or 'take' in command) and ('photo' in command or 'selfie' in command or 'picture' in command or 'image' in command or 'pic' in command)):
        capture_image()

    elif 'weather report' in command and 'google' not in command and 'youtube' not in command:
        weather_report()

    elif 'play' in command and 'song' in command:
        play_song()

    elif (('search' in command  or 'find' in command or 'display' in command or 'show' in command) and ('youtube' not in command)):
        search(command,'google')

    elif (('search' in command or 'find' in command or 'display' in command or 'show' in command) and ('youtube' in command)):
        search(command,'youtube')

    elif 'screenshot' in command:
        screenshot_name = ctime()+'.png'
        take_screen_shot(screenshot_name)
        manage_image(screenshot_name)

    elif 'open' in command and ('app' in command or 'application' in command):
        app = take_command('which application would you like to open')
        open_app(app)

    elif 'wikipedia' in command or 'wiki' in command:
        get_wiki(command)
    
    elif 'news' in command and 'google' not in command and 'youtube' not in command:
        get_news_feeds()

    elif feedback(command):
        return True

if __name__ == '__main__':

    # response = initiate()
    response = '200'
    if response == '200':
        greet()
        while True:
            print('Speak Now ...')
            command = take_command()
            if name in command:
                command = command.replace(name,'')
            print(f'you said : {command}')
            execute_command(command)
    else:
        custom_exit()