from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.contrib import messages
import datetime

from django.test import TestCase
from django.contrib.auth import authenticate, login, logout
import random, string
from django.contrib.auth.models import User

# Create your tests here.
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition


def zara(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    
    engine.runAndWait()
    return None

def jarvis(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
    return None

def wishMe(request, speak, name):
    a = ''
    if request.user.is_superuser == True:
        if name == 'zara':
            a = 'boss'
        else:
            a = 'sir'    
        pass
    elif request.user.is_staff == True:
        a = 'sir'
        pass
    elif request.user.is_authenticated:
        a = str(request.user)
        pass

    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak(f"Good Morning,{a}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon,{a}")   

    else:
        speak(f"Good Evening,{a}")  

    #speak(f"I am {name}. Please tell me how may I help you")


#query = takeCommand().lower()
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
        
    except Exception as e:
        print(e)    
        print("Say that again please...")  
        query = "Say that again please..."


    return query




def homeIndex(request):

    #print("Loading")
    
    try:
       
        wishMe(request, zara, "zara")
        #jarvis("Welcome To The Tournament zone.")
        #zara("I am zara. Tell me how may i help you")
                
    except Exception as e:
        print("error", e)
        pass

    #messages.success(request, 'Welcome')        
    return render(request, 'home/homeIndex.html')

def hadleLogin(request):
    if request.user.is_authenticated:
        messages.info(request, 'Logout your Account First')
        return redirect('/')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Successfully Logged In")
            return redirect('/Account/')
        else:
            messages.error(request, 'Try Again') 
            return redirect('/')
    return HttpResponse("Ok")

def handleLogout(request):
    logout(request)
    return redirect('/')