import  speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener =sr.Recognizer()
engine =pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            #talk(command)
            print(command)
            return command
    except:
        pass

def playing():
    comm=take_command()
    print(comm)
    if 'play' in comm:
        music=comm.replace('play','')
        talk('playing'+music)
        print(music)
        pywhatkit.playonyt(music)
    elif 'time' in comm:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is:'+time)
    elif 'date' in comm:
        time = datetime.datetime.now().strftime('%B:%A:%Y')
        time1 = datetime.datetime.now().strftime('%m:%d:%Y')
        talk('current DATE  is:' + time+time1)

    elif 'who is'in comm:
        man=comm.replace('who is','')
        info=wikipedia.summary(man,10)
        talk(info)
    elif 'joke'in comm:
        talk(pyjokes.get_joke())
    else:
        print('please say again')
playing()