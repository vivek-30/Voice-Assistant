import requests
import cv2
from time import sleep,ctime
from core_functions import speak,take_command
from PIL import Image
from CLI_Functions import remove

def read_news_feeds(feeds):
    total_feeds = feeds['totalResults']
    if (total_feeds <= 0):
        speak('no news feed available')
    else:
        speak(f'there are total {total_feeds} news update how many feeds do you want to hear')
        total = int(input('=> '))
        if total > total_feeds or total <= 0:
            speak('sorry but you have demanded non feasible amount')
        else:
            feeds = feeds['articles']
            for feed in range(total):
                title = feeds[feed]['title']
                description = feeds[feed]['description']
                content = feeds[feed]['content']
                speak(f'title of news number {feed+1} is {title}')
                speak(f'description of this news is {description}')
                speak(f'content of this news is {content}')
            speak('thats all sir hope you have enjoyed our service')

def get_news_feeds():
    URL = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=01ca42aa1b41426185867f49a1dfc499'
    response = requests.get(URL).json()
    if response['status'] == 'ok':
        read_news_feeds(response)
    else:
        speak('sir there is some problem in fetching news feed please try after some time')

def delete_image(image_name):
    answer = take_command('would you like to save this picture').strip()
    if answer == 'no' or answer == 'discard' or answer == 'never' or answer == 'dont':
        sleep(3)
        remove(image_name)

def manage_image(image_name):
    img = Image.open(image_name)
    img.show()
    delete_image(image_name)

def capture_image():
    camera = cv2.VideoCapture(0)
    sleep(0.8) # waits untill camera is completly opened.
    result_value, image = camera.read()
    del(camera)
    image_name = ctime()+'.jpg'
    cv2.imwrite(image_name, image)
    manage_image(image_name)
