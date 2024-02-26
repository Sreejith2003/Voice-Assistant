import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pyautogui
import sys

# For Voice Recognition

engine=pyttsx3.init('sapi5')       # sapi5 is a microsoft inbuilt voice
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) # 0 = male, 1 = female


# speak function

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
        
# wishing function

def wishMe():    #defining a program as wish me 
    hour=datetime.datetime.now().hour
    strTime=datetime.datetime.now().strftime("%H:%M") 
    if hour>=0 and hour<12:
        speak(f"Good Morning Sir,its {strTime} in the morning")
        print(f"Good Morning Sir,its {strTime} in the morning")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon Sir,its {strTime} in the afternoon")
        print(f"Good Afternoon Sir,its {strTime} in the afternoon")
    else:
        speak(f"Good Evening Sir, its {strTime} in the evening")
        print(f"Good Evening Sir, its {strTime} in the evening")
        

# Function to take command

def takeCommand():   # this program for the use of microphone
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source,timeout=5,phrase_time_limit=8)

        try:
            statement=r.recognize_google(audio,language='en-in')      # en-us uses american english we can also use en-in for indian english
            print(f"user said:{statement}\n")
            

        except Exception as e:
            speak("Pardon me, please say that again")
            print("Pardon me, please say that again")
            return "None"
        return statement.lower()
    

# Main loop

if __name__=='__main__':
    
    while True:
        statement = takeCommand().lower()
        if "wake up" in statement:
            wishMe()
            speak("Hi sreejith how can i help you?")
            print("Hi sreejith how can i help you?")
            continue
            
               

        if "go to sleep" in statement:
                    statement = takeCommand()
                    speak("Ok sir, you can call me anytime")
                    print("Ok sir, you can call me anytime")
                    break
                    
        # To search wikipedia
           
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            print('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")    # this line used to remove the word wikipedia when we search for something
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print("According to Wikipedia")
            print(results)
            speak(results)
            
        # To stop the voice assistant
            
        if "stop" in statement:
            speak("Your personal assistant is now shutting down")
            print("Your personal assistant is now shutting down")
            break
            
        # To open and close the youtube

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com/")
            speak("youtube is now opening...")
            time.sleep(5)

        elif "close youtube" in statement:
            pyautogui.hotkey('ctrl', 'w')   # pyautogui is used to press the keys
            speak("Closing the youtube...")
            print("Closing the youtube...")
            
        # To open and close the google

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            print("Google chrome is open now")
            time.sleep(5)
            
        elif "close google" in statement:
            pyautogui.hotkey('ctrl', 'w')
            speak("Closing the tab in google...")
            print("Closing the tab in google...")
            
        # To open and closing the Gmail 

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            print("Google Mail open now")
            time.sleep(5)
            
        elif "close gmail" in statement:
            pyautogui.hotkey('ctrl', 'w')
            speak("Closing all the gmail...")
            print("Closing all the gmail...")
            
            
        elif "Open LinkedIn" in statement:
            webbrowser.open_new_tab("https://www.linkedin.com/feed/")
            speak("linkedin is opening...")
            print("linkedin is opening...")
            
            
        # Weather

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            print("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        # Time

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")  # str - String format in hr,min,sec
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am S20 version 1 point O your persoanl assistant, who is made by sreejith I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Sreejith, by using python")
            print("I was built by Sreejith, by using python")

        # To open Stackoverflow

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
            print("Here is stackoverflow")
            
            
        # To Switch the window
            
        elif "switch the window" in statement:
            speak("Switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")



        # To open news

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            print('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        # To open camera
        
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")
            speak("Photo taken successfully.")
            print("Photo taken successfully.")
            camera_on = True  # Set the flag to keep the camera on
            
        # Note taking 

        elif "log" in statement or "take a note" in statement:
            speak("What is the name of the note: ")
            note_name = takeCommand().lower()
            file_name = f"{note_name}.txt"
            speak(f"ready to record your note for{note_name}")
            newnote = takeCommand().lower()
            with open(file_name, "w") as newfile:
                newfile.write(newnote) 
                speak(f"'{note_name}' has been written")
                
        # TO delete the note or a file
                
        elif "remove" in statement or "delete the note" in statement:
            speak("Sure, please tell me the name of the note you want to delete.")
            print("Sure, please tell me the name of the note you want to delete.")
            file_name = takeCommand()
            os.remove(f"{file_name}.txt")
            speak("The file is been deleted")
            print("The file is been deleted")

            
        # to open and close the file explorer
        
        elif "open file" in statement:
            os.system("explorer")
            speak("The file explorer is opening...")
            print("The file explorer is opening...")
            
        elif "close the file" in statement:
            statement = os.system("taskkill /f /im explorer.exe")
            speak("Closing file explore..")
            print("Closing file explore..")
            
        # To open and close the Notepad  
          
        elif "open notepad" in statement:
            os.system("notepad")
            speak("Notepad opening...")
            print("Notepad opening...")
        
        
        elif "close notepad" in statement:
            os.system("taskkill /f /im notepad.exe")
            speak("Closing notepad....")
            print("Closing notepad....")
            
        # To search in google

        elif 'search'  in statement or 'browser' in statement:
            speak("What do you wnat to search about?")
            print("What do you wnat to search about?")
            search = takeCommand().lower()
            print(f"searching {search}")
            webbrowser.open(f"https://www.google.com/search?q={search}")
            time.sleep(5)
        

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            print('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="XT5U2Y-KL68V3EEJ2"
            client = wolframalpha.Client('XT5U2Y-KL68V3EEJ2')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        # To shutdown the system or lap 

        elif "off" in statement or "shutdown" in statement:
            speak("The computer will shutting down in 10 seconds, make sure all the tabs are closed")
            subprocess.call(["shutdown","/s","/t","10"]) 
            
        # To sign out or sleep the system or lap 

        elif "sleep" in statement or "sign out" in statement:
            speak('Ok , your pc will log off in 10 seconds make sure you exit from all applications')
            print('Ok , your pc will log off in 10 seconds make sure you exit from all applications')
            subprocess.call(["shutdown", "/l", "/t", "10"]) 
            
time.sleep(5)


