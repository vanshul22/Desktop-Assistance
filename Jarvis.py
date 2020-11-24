"""
Project Name : Desktop Assistant.
Author : Vanshul Kesharwani
Date : 28/07/2020
Language : Python 3.7.1
Details : This is an Artificial Assistant for Voice Commands.
version : 0.1
"""


import pyttsx3   # from gtts import gTTS
import datetime  #  built in
import speech_recognition as sr
import wikipedia
import webbrowser  # in built
import os
import random
import time
import platform
import socket
# import warnings

# Ignore any warning messages
# warnings.filterwarnings("ignore")  # Check in google

# For replying from random.choices
hello_list_1 = ["hi", "hello", "namaste", "hello", "hi", "namaste", "hola", "aloha"]


# Taking speak language from computer.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    """
    Take Argument as Text and speak that word by speakers.
    """
    engine.say(audio)
    engine.runAndWait()


def wishme():
    """
    Take time from computer and greet from time.
    """
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        print("Hello, Good Morning Boss.")
        speak("Hello, Good Morning Boss.")

    elif 12 <= hour < 17:
        print("Hello, Good After Noon Boss.")
        speak("Hello, Good After Noon Boss.")

    elif 17 <= hour < 20:
        print("Hello, Good Evening Boss.")
        speak("Hello, Good Evening Boss.")

    else:
        print("Hello, Namaste Boss.")
        speak("Hello, Namaste Boss.")

    speak("I am Jarvis. Your Desktop Assistant. Storage 0.5 Terra Byte, Memory 4 Geega Byte, Speed 1.5 Geega Hertz,\nPlease tell me how may help you, Boss.")



def takecommand():
    """
    Taking command from microphone from user and return string.
    """
    global query
    r = sr.Recognizer()  # Recogniser class helps us to recognise input audios from user.
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source, phrase_time_limit=5)

    # Blank Query for Exception handling
    query = ""

    # Using Google Speech Recognition
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said : {query}\n")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not Understand the Audio!!!")

    except sr.RequestError:
        print("Couldn't Request Results\nTurn on Your Internet Connection!!!")

    return query


if __name__ == "__main__":
    
    wishme()
    # if 1:
    while 1:
        query = takecommand().lower()
        # query = input("listening.......\n")

        # Executing Task based on Query #

        # For understand hi, hello, namaste type words.
        split_query = query.split(" ")
        for i in split_query:
            if i in hello_list_1:
                random_greet = f"{(random.choice(hello_list_1)).title()} Boss"
                print(random_greet)
                speak(random_greet)
                        
        if "command" in query:
            print("\nMy Commands are:\n\nWhat can I do for you;\n(Speak_Your_Search) Wikipedia,\nOpen and Close - Google, Youtube, Opera,\nOpen and Close - Music, VS Code, VLC Player,\nSystem Detail, IP Address, Repeat (Query),\nDate and Time, Shutdown, Restart,\nSay - Very Good, Excellent, Thankyou, Good,\nQuit, Tata, Bye Bye.")
            speak("\nMy Commands are:\n\nWhat can i do for you,\n(Speak Your Search) Wikipedia,\nOpen and Close - Google, Youtube, Opera,\nOpen and Close - Music, VS Code, VLC Player,\nSystem Detail, IP Address, Repeat My Words (Query),\nDate and Time,\nShutdown, Restart\nSay - Very Good, Excellent, Thankyou, Good,\nQuit, Tata, Bye Bye.")

        if "what can" in query:
            print("\nI can do this following for you: \nOpen Applications,\nGoogle Search, Wikipedia Search,\nCurrent Date and Time, Play Music,\nSystem Details, IP Address, Repeat Your Words,\nShut Down and Restart Laptop.")
            speak("\nI can do this following for you, Open Applications, Google Search, Wikipedia Search, Current Date and Time, Play Music, System Details, IP Address, Repeat Your Words, Shut Down and Restart Laptop.")

        if "wikipedia" in query:
            print("Searching on Wikipedia...")
            speak("Searching on Wikipedia...")
            query = query.replace("wikipedia ", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if "open youtube" in query:
            print("Opening YouTube")
            speak("Opening YouTube")
            webbrowser.open("www.youtube.com")

        if "google" in query:

            if "open google" in query:
                print("What do you Want to Search ?")
                speak("What do you Want to Search ?")
                search = takecommand().lower()
                print("Searching...")
                speak("Searching...")
                url = "https://google.com/search?q=" + search
                webbrowser.open(url)
            
            if "close google" in query:
                os.system("TASKKILL /F /IM chrome.exe")

        if "opera" in query:

            if "open opera" in query:
                opera_dir = "C:\\Program Files (x86)\\Opera\\launcher.exe"
                print("Opening Opera Browser")
                speak("Opening Opera Browser")
                os.startfile(opera_dir)

            if "close opera" in query:
                print("Closing Opera Browser")
                speak("Closing Opera Browser")
                os.system("TASKKILL /F /IM Opera.exe")

        if "youtube search" in query:
            pass

        if "music" in query:

            if "play music" in query or "open music" in query:
                print("Opening Music")
                speak("Opening Music")
                music_dir = "E:\\Musico\\new audio"
                songs = os.listdir(music_dir)
                # print(songs)
                randem_song = random.randint(0, (len(songs)))
                os.startfile(os.path.join(music_dir, songs[randem_song]))

            if "stop music" in query or "close music" in query:
                print("Closing Music")
                speak("Closing Music")
                os.system("TASKKILL /F /IM Music.UI.exe")

        if "date" in query:
            strTime = datetime.datetime.now()
            print(f"\nSir, The Date is {strTime.day}-{strTime.month}-{strTime.year}")
            speak(f"Sir, Today's {strTime.day}, Month is {strTime.month}, Year is {strTime.year}")
        
        if "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"\nSir, The Time is {strTime}")
            speak(f"Sir, The Time is {strTime}")

        if "code" in query:

            if "open vs code" in query:
                codepath = "C:\\Users\\Vanshul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
                print("Opening VS CODE")
                speak("Opening VS CODE")

            if "close vs code" in query:
                print("Clossing VS Code")
                speak("Clossing VS Code")
                os.system("TASKKILL /F /IM code.exe")

        if "player" in query:

            if "open vlc player" in query:
                codepath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
                print("Opening VLC Player")
                speak("Opening VLC Player")
                os.startfile(codepath)

            if "close vlc player" in query:
                print("Closing VLC Player")
                speak("Closing VLC Player")
                os.system("TASKKILL /F /IM vlc.exe")
        
        if "system detail" in query:
            print(f"\n{platform.system()}", end="")  # Software type Windows , Linux, IOS
            speak(platform.system())
            print(f" - {platform.machine()}")  # Type of Processor
            speak(platform.machine())
            print(platform.architecture())  # Type of Software
            print(platform.node())   # Name of Computer.
            speak(platform.node())
            print(platform.processor())  # Processor Details.
            print(platform.uname()) # all above Details
            print("Python Version -",end=" ")
            print(platform.python_version())  # Python Version
            speak("Python Version")
            speak(platform.python_version())
        
        if "ip address" in query:
            hostname = socket.gethostname()  # Coputername
            ipaddr = socket.gethostbyname(hostname)  # ip addresss
            print("Computer Name: ", hostname)
            speak("Computer Name")
            speak(hostname)
            print("IP Address:", ipaddr)
            speak("IP Address")
            speak(ipaddr)
        
        if "repeat" in query:
            query = query.replace("repeat ", "")  
            print(query)
            speak(query)
        
        if "very good" in query or "excellent" in query or "thank you" in query or "good" in query:
            print("Thankyou Boss")
            speak("Thankyou Boss")
            
        if "close" in query:
            queryc = query.replace("close ","")
            queryc = f"{(queryc).lower()}.exe"
            os.system(f"TASKKILL /F /IM {queryc}")

        if "shut down" in query or "shutdown" in query:
            shut = input("\nReally Want to Shutdown:(Y/N):\n>>> ").lower()
            if shut == "y":
                print("\nClossing VS Code,")
                speak("Clossing VS Code")
                print("Shutting Down Computer,")
                speak("Shutting Down Computer")
                os.system("TASKKILL /F /IM code.exe")
                os.system("shutdown /s /t 10")

        if "restart" in query:
            res = input("\nDo You Really Want to Restart:(Y/N):\n>>> ").lower()
            if res == "y":
                print("\nClossing VS Code,")
                speak("Clossing VS Code")
                print("Re-starting Computer,")
                speak("ReStarting Computer")
                os.system("TASKKILL /F /IM code.exe")
                os.system("shutdown /r /t 10")

        if "quit" in query or "bye" in query or "tata" in query:
            print("Thankyou Boss...\nBye Bye...")
            speak("Thankyou Boss...\nBye Bye...")
            quit()

        # else:
        #     print("Your Enter Voice is Wrong.")
        #     speak("Your Enter Voice is Wrong.")
        print()
        time.sleep(2)
