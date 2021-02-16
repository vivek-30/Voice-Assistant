import os
from time import sleep
from sys import platform
from subprocess import call
from random import randrange

def open_app(app):
    app_path = os.path.expanduser('~')+'/../../Applications/'+app+'.app' 
    if platform == "darwin":
        call(['open', app_path])

def start_mysql_server():
    if platform == "darwin":  
        call(['mysql.server', 'start']) # open mysql server
        sleep(4) # Wait for 4 seconds

def stop_mysql_server():
    if platform == "darwin":  
        call(['mysql.server', 'stop']) # open mysql server
        sleep(4) # Wait for 4 seconds

def take_screen_shot(screenshot_name):
    if platform == "darwin":
        call(['screencapture', screenshot_name])

def play_song():
    random_num = 0
    music_folder = os.path.expanduser('~')+'/Documents/Songs/'
    songs = os.listdir(music_folder)
    random_num = randrange(0,len(songs))
    music_folder = music_folder + songs[random_num]
    if platform == "darwin":
        call(['open', music_folder])

def weather_report():
    if platform == "darwin":
        call(['curl', 'https://wttr.in'])

def uptime():
    if platform == "darwin":
        call(['uptime'])

def remove(file_name):
    if platform == "darwin":
        call(['rm', file_name])