from django.test import TestCase

# Create your tests here.
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning,boss")

    elif hour>=12 and hour<18:
        speak("Good Afternoon,boss")   

    else:
        speak("Good Evening,boss")  

    speak("I am zaaara. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
   
    r = sr.Recognizer()     
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
           

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        query = e
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('indranil.techwork@gmail.com', 'INDRANIL1.')
    server.sendmail('indranil.techwork@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        print("my query",query)
        

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("ok boss")
            webbrowser.open("youtube.com")
    
            
        elif 'open google' in query:
            speak("ok boss")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("ok boss")
            webbrowser.open("stackoverflow.com")

       
            
        elif 'who are you' in query:
            speak("I am zaaara. if you have any quary please tell my boss")

        elif 'hey' in query:
            speak("Yes,boss. Please tell me how may I help you")
 
        elif 'boss' in query:
            speak("my boss is neel. he created by me, his own style! he is a great human also, and we all love him ")

        elif 'play music' in query:
            try:

                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
               
                os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                speak("Sorry I cant found Any type music library in your system")    
         
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"boss, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            """

        elif 'email to nil' in query or 'email to neil' or 'mail to neil' or 'mail to nil':
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "indranil.swarnakar@gmail.com"
                speak(content)
                speak('Boss Can I Send This Message')
                myquery = takeCommand()
                print(myquery)
                if myquery == 'yes':
                    pass
                    
                elif myquery == 'no':
                    speak('Ok Boss. You Have Any Task For Me')
                    myquery = takeCommand()
                    if myquery == 'no':
                        query = takeCommand()

                        
                    else:
                        content = takeCommand()
                        speak(content)
                            
                        


                
                sendEmail(to, content)
                speak(" Boss Email has been sent Successfully!")        
                    
                    
              


                
               
            except Exception as e:
                #print(e)
                speak("Sorry Boss. I am not able to send this email")
                speak(e)
        """

        elif 'open my admin' in query:
            speak('trying boss')
            webbrowser.open("getsitefly.com/admin/")
        
            

