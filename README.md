## Voice Assistance

- A fully automated Voice Assistance ( Jarvis ) built with python.

- It will help you handle your task easily and efficiently and makes your life easy.

## Prerequisite -

- Must have `MySQL` installed in your system. (it will need to authenticate jarvis users) 

- `Internet Connectivity` should be provided.

- last but not the least `Python` is a must have requirement for this to work.

## Setup and Installation -

- Install MySQL [click here to Download](https://www.mysql.com/downloads/) ( for Mac OS users  `brew install mysql` if brew is installed )

- start your mysql server with `mysql.server start`

- create a database named jarvis_users 
```
    mysql -u root

    create database jarvis_users;

    use jarvis_users;

    create table users(
        admin char(3) default "NO",
        name varchar(30) primary key,
        password varchar(30) unique not null, 
        gender char(1) default 'M'
    );

    exit;
```

- install portaudio `brew install portaudio` (only for Mac OS X users)

- clone the repo and navigate into it

- install all dependencies `pip3 install -r requirements.txt`

- lastly make sure you have connected to a decent internet connection.
- 🥳 Wooho you have completed all the steps now just run this last command `python3 main.py` in your CLI (teminal,command prompt).

## Features -

- MySQL Support (To authenticate Jarvis users)
- Google Search Support
- Wikipedia Support
- Get News Update
- Youtube Support
- Command Line Support
- Get Weather report
- Feedback Support
- Get Time Update
- Open any app
- Listen any Song
- Create any file and write content inside it
- Capture Photos
- Capture ScreenShots
- Explore More.

## Usage - 

- Tell me the time
- Tell me your name
- Play a song
- Give/Provide me the weather report
- Capture/Take/Click a photo/picture
- Capture screenshot
- Search/Find/Show < anything > on/in google
- Search/Find/Show < anything > on/in youtube
- Gave me wikipedia of < something >
- Can give feedback like good job, nice work , poor service
- Give/Provide News Update/Feeds
- Create a file
- Open a App/Application
- Exit

#### Note  - 

- Above mentioned command are not very strict their is much flexibily exists. These are just for Refference.

- some IDE dont allow you to use your default microphone in this case you must run this service from Command Line

- Dont forget to stop mysql server after the usage of this service `mysql.server stop`

