import webbrowser
import wikipedia
from core_functions import speak

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

def search(command,search_place):
    search_item = manage_search(command)
    if search_place == 'google':
        url = f"https://google.com/search?q={search_item}"
    elif search_place == 'youtube':
        url = f"https://youtube.com/results?search_query={search_item}"
    else: return

    if search_item:
        webbrowser.get().open(url)
        speak(f'these are the results for {search_item} on {search_place}')
    else:
        speak('empty search is redundant')
    
def get_wiki(command):
    command = command.replace('wikipedia','')
    if 'give me' in command:
        command = command.replace('give me','')
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
