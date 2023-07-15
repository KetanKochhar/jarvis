import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello, good morning")
        print("Hello, Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Hello, good afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, good evening")
        print("Hello, Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Sorry, could not understand. Please say that again.")
        return "None"
    return query


def openBrowser():
    speak("Opening web browser")
    webbrowser.open("https://www.google.com")


def searchWikipedia():
    speak("What would you like to search on Wikipedia?")
    query = takeCommand()
    if query != "None":
        try:
            speak(f"Searching Wikipedia for {query}")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Multiple options found. Please provide a more specific query.")
        except wikipedia.exceptions.PageError as e:
            speak("No results found. Please try a different query.")
        except Exception as e:
            speak("Sorry, could not complete the search.")




def openYouTube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")


if __name__ == '__main__':
    wishMe()
    speak("Tell me how may I help you, sir ?")

    while True:
        query = takeCommand().lower()
        if query == "None":
            continue
        elif "good bye" in query or "ok bye" in query or "stop" in query or "shut up" in query or "don't talk" in query:
            speak('Your personal assistant is shutting down. Goodbye!')
            print('Your personal assistant is shutting down. Goodbye!')
            break
        elif "open browser" in query:
            openBrowser()
        elif "search wikipedia" in query:
            searchWikipedia()
        elif "open youtube" in query:
            openYouTube()