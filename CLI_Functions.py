import os
import sys
from subprocess import call
from random import randrange

def open_app(app):
    app_path = os.path.expanduser('~')+'/../../Applications/'+app+'.app' 
    if sys.platform == "darwin":
        call(['open', app_path])

def take_screen_shot(screenshot_name):
    if sys.platform == "darwin":
        call(['screencapture', screenshot_name])

def play_song():
    random_num = 0
    music_folder = os.path.expanduser('~')+'/Documents/Songs/'
    songs = os.listdir(music_folder)
    random_num = randrange(0,len(songs))
    music_folder = music_folder + songs[random_num]
    if sys.platform == "darwin":
        call(['open', music_folder])

def weather_report():
    if sys.platform == "darwin":
        call(['curl', 'https://wttr.in'])

def uptime():
    if sys.platform == "darwin":
        call(['uptime'])

def remove(file_name):
    if sys.platform == "darwin":
        call(['rm', file_name])