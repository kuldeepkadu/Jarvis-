import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("good Evening!")

    speak("I'm Jarvis. Please tell me how i help you?")


def takeCommand():
    #takes microphone input from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")

    except Exception as e:
        print(e)
        print("Not Recognized, Say That Again Please...")
        speak("Say That Again Please...")
        return "None"
    return query

def sendemail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    speak("Hey KULDEEP!")
    wishMe()
    takeCommand()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentances=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube'  in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stakeoverflow' in query:
            webbrowser.open("stakeoverflow.com")

        elif 'play music' in query:
            music_dir ='E:\\Taylor Songs\\Taylor Songs'
            songs =  os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, The Time is : (strTime)")


        elif 'open pycharm' in query:
            codePath =  "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.1\\bin\]pycharm64.exe"
            os.startfile(codePath)

        elif 'open sublime' in query:
            codePath = "F:\\installed\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)



        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "your_email@gmail.com"
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception in e:
                print(e)
                speak("Sorry Email has not send, Try after some time.")
















