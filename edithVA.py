import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import pyjokes
import wikipedia
import subprocess

id ='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        said = r.listen(source)
        try:
            print('I am listening')
            q = r.recognize_google(said, language="en")
            return q
        except sr.UnknownValueError:
            print("Sorry I did not understand")
            return "I am waiting"
        except sr.RequestError:
            print('Sorry the service is down')
            return "I am waiting"
        except:
            return "I am waiting"
        
def speaking(message):
    engine = pyttsx3.init()
    engine.setProperty('voice',id)
    engine.say(message)
    engine.runAndWait()
    
def query_day():
    day = datetime.date.today()
    #print(day)
    weekday = day.weekday()
    #print(weekday)
    mapping = {
        0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'
    }
    try:
        speaking(f'Today is {mapping[weekday]}')
    except:
        pass

def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speaking(f"{time[0:2]} o'clock and {time[3:5]} minutes")

def whatsup():
    speaking('''Hi, I am edith.
    I am at your service, boss
    ''')

def emotion():
    cmd = "python test.py"
    p = subprocess.Popen(cmd,shell=True)
    return p

#the heart of our assistant. Takes queries and returns answers
def querying():
    whatsup()
    start = True
    while(start):
        q = transform().lower()
        
        if 'open youtube' in q:
            speaking('starting youtube. Just a second.')
            webbrowser.open('https://www.youtube.com')
            continue
            
        elif 'go google' in q:
            speaking('opening browser')
            webbrowser.open('https://www.google.com')
            continue
        
        elif 'what day is it' in q:
            query_day()
            continue
        
        elif 'emotion detection' in q:
            speaking("active detecion , just wait")
            emotion()
            continue
            
        elif 'what time is it' in q:

            query_time()
            continue
            
        elif "shut down" in q:
            speaking('ok I am shutting down')
            break
        
        elif "from wikipedia" in q:
            speaking('checking wikipedia')
            q = q.replace("wikipedia","")
            result = wikipedia.summary(q,sentences=2)
            speaking('found on wikipedia')
            speaking(result)
            continue
        
        elif "your name" in q:
            speaking('I am edith. Your VA')
            continue
            
        elif "search web" in q:
            pywhatkit.search(q)
            speaking('that is what I found')
            continue
            
        elif "play" in q:
            speaking(f'playing {q}')
            pywhatkit.playonyt(q)
            continue
            
        elif "joke" in q:
            speaking(pyjokes.get_joke())
            continue
            
        elif "vision game" in q:
            cmd = "python cvgame.py"
            speaking("opening game")
            subprocess.Popen(cmd)
            continue
    
    
    
querying()

    
    
    
    
    
    
    
    
    
    
    
    
    
    