import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener=sr.Recognizer()
engine=pyttsx3.init()
    
    
def talk(text):
    
    engine.say(text)
    engine.runAndWait()
def take_command():    
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'friday' in command:
                command=command.replace('friday','')

                print(command)

    except:
        pass    
    return command
def run_friday():
    command=take_command()    
    if 'play' in command:
        song=command.replace('hey','')
        song=command.replace('play','')
        talk('playing'+song)
        print('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')    
        print(time)
        talk('current time is'+time)
    elif 'who is' in command :
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'tell me about' in command :
        person=command.replace('tell me about','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'what is' in command :
        person=command.replace('what is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)    
    elif 'hey' or 'hello' or 'hi' in command:

        engine.say('hey boss, i am friday! ur virtual voice assistant')
        engine.say('what can i do for you?')
        engine.runAndWait()
    else:
        engine.say('can u please repeat your command?')
        engine.runAndWait()

       
while True: 
    run_friday()                                                           