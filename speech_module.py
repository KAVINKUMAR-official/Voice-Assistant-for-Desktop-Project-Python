import pyttsx4
import speech_recognition as sr
import datetime
import colorama
from colorama import Fore, Style


engine = pyttsx4.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to convert text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user based on the time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you today?")



def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.GREEN + "Listening..." + Style.RESET_ALL)
        recognizer.pause_threshold = 1.5  # Response time
        recognizer.energy_threshold = 150  # Noise reduction
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjusts for ambient noise

        try:
            # Set a timeout (e.g., 5 seconds) for waiting to start listening, and a phrase time limit (e.g., 10 seconds)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print(Fore.YELLOW + "Recognizing..." + Style.RESET_ALL)
            query = recognizer.recognize_google(audio, language='en-in')
            print(Fore.CYAN + f"User said: {query}\n" + Style.RESET_ALL)
        except sr.UnknownValueError:
            print(Fore.RED + "Sorry, I did not catch that. Please say that again..." + Style.RESET_ALL)
            return "None"
        except sr.RequestError:
            print(Fore.RED + "Could not request results from Google Speech Recognition service." + Style.RESET_ALL)
            return "None"
        except sr.WaitTimeoutError:
            print(Fore.RED + "Listening timed out while waiting for speech." + Style.RESET_ALL)
            return "None"
        
    return query
