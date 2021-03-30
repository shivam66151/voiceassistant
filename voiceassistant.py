
import pyttsx3                   #text to speech library
import datetime
import speech_recognition as sr
import webbrowser
import subprocess
import os
import pywhatkit
import wikipedia
import smtplib

engine=pyttsx3.init('sapi5')              #Sapi5 is microsoft develop speech Api
voices=engine.getProperty('voices')       
engine.setProperty('voice',voices[1].id)  #Setting male voice


#Creating Speak() Function to give Speaking power to our voice assistant
def speak(audio):
    engine.say(audio)     #Anything we pass inside engine.say() will be spoken by voice assistant
    engine.runAndWait()   #without this query speech will not be audible to us


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Alexa sir,Please tell me how can i help you")


def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sharmashivam66151@gmail.com','emailidshivamsharma8055')
    server.sendmail('sharmashivam66151@gmail.com',to,content)
    server.close()


def take_query():
    #It takes microphone input from user and  returns string output

    listener=sr.Recognizer()             #Initiliazing speech_recognition
    with sr.Microphone() as source:      #opening physical microphone of computer
        print("Listening....")
        listener.pause_threshold = 1
        audio =listener.listen(source)   #storing audio/sound in voice variable
        try:
            print("Recognizing")
            query=listener.recognize_google(audio, language='en-in') #using google for voice recognition
            print(f"User said: {query}\n")          

        except Exception as e:
            print(e)
            print("Say that again please...")  #say that again will be printed in case improper voice
            return "None"
    return query

#Driver Code
if __name__ == '__main__':
    wishMe()

    while True:

        # All the command said by user will be stored here in 'query' and will be converted to lower case for easily
        # recognition of command
        query = take_query().lower()
        #logic for executing tasks based on query
        if "youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "play music" in query:
            speak("Here you go with music sir")
            music_dir='C:\\Users\sharm\OneDrive\Documents\music\Playlists'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "play" in query:    #if play found in query than this block will be executed
            song=query.replace('play','')
            speak('playing' +song)
            pywhatkit.playonyt(song)
        elif "email to shivam" in query:
            try:
                speak("What should I say?")
                content = take_query()
                to = "sharmashivam66151@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
        elif "time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak('Current Time is' +time)
        elif 'who is' in query:
            speak("Searching")
            person = query.replace('who is', '')
            info = wikipedia.summary(person, sentences= 1)
            speak("According to Wikipedia")
            print(info)
            speak(info)
        elif "how are you" in query:
            speak("I am Fine,Thank you")
            speak("How are you?")
        elif "fine" in query or "good" in query:
            speak("It's good to know you are fine")
        elif "what's your name" in query or "who are you" in query:
            speak("My name is Alexa")
        elif "exit" in query:
            speak("Thanks for giving your time")
            exit()
        elif "are u single" in query:
            speak("I am in relationship with wifi")
        elif "who made you" in query:
            speak("I have been created by Shivam")
        elif "who am i" in query:
            speak("if you talk then definitely you are human")
        elif "why you came to world" in query:
            speak("Thanks to Shivam,further it's a secret")
        elif "what is love" in query:
            speak("It is 7th sense which destroys  al other senses")
        # elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
        elif "i love you" in query:
            speak("It's hard to understand")

            





















