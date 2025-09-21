import webbrowser
import wikipedia
import pyjokes
import os
import datetime
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from speech_module import speak

# Initialize NLP components
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Download necessary resources for nltk
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# Preprocess query using NLP
def preprocess_query(query):
    tokens = word_tokenize(query.lower())
    filtered_tokens = [word for word in tokens if word not in stop_words]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    processed_query = ' '.join(lemmatized_tokens)
    return processed_query


# Perform tasks based on the query

def perform_task(query):
    query = preprocess_query(query)

    if 'open youtube' in query:
        speak('Opening YouTube')
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        speak('Opening Google')
        webbrowser.open("https://www.google.com")

    elif 'instagram' in query:
        speak('Opening Instagram')
        webbrowser.open("https://instagram.com")

    elif 'facebook' in query:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif 'search for' in query or 'google' in query:
        search_term = query.replace("search for", "").replace("google", "").strip()
        if search_term:
            speak(f"Searching Google for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        else:
            speak("What do you want to search for?")

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "").strip()
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple results for this. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find anything on Wikipedia about that.")

    elif "joke" in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    # system Folder and files
    elif "open desktop" in query or "desktop" in query:
        speak("opening Desktop Folder")
        folder_desktop="c:\\users\\KAVIN KUMAR\\Desktop"
        os.startfile(folder_desktop)
    elif "open documents" in query or "documents" in query:
        speak("opening Document Folder")
        folder_documents="c:\\users\\KAVIN KUMAR\\Documents"
        os.startfile(folder_documents)
    elif "open downlods" in query or "downloads" in query:
        speak("Opening Downloads Folder")
        folder_downloads="c:\\users\\KAVIN KUMAR\\Downloads"
        os.startfile(folder_downloads)
        

    # System Applications 

    elif 'open notepad' in query:
        speak("Opening Notepad")
        os.startfile('C:\\Windows\\system32\\notepad.exe')

    elif 'open browser' in query or 'open web browser' in query:
        speak("Opening Web browser")
        os.startfile('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')

    elif 'open excel' in query or 'open microsoft excel' in query:
        speak("Opening M S excel")
        os.startfile('C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.EXE')

    elif 'open word' in query or 'open microsoft word' in query:
        speak("Opening M S word")
        os.startfile('C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE')

    elif 'open PPT' in query or 'open power point' in query or'open powerpoint' in query :
        speak("Opening M S Power Point")
        os.startfile('C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.EXE')



    elif 'play music' in query:
        music_dir = 'C:\\Users\\Admin\\Desktop\\Voice Assistant 2.0\\Songs'
        songs = os.listdir(music_dir)
        if songs:
            speak('Playing music')
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak('No music found in the directory.')

    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        speak(f"The time is {current_time}")

    elif 'date' in query:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(current_date)
        speak(f"The date is {current_date}")

    elif 'shutdown the system' in query or 'shut down the system' in query:
        speak("Shutting Down the System")
        os.system("shutdown /s /t 1")

    elif "restart the system" in query or "re start the system" in query:
        speak("Restarting the System")
        os.system("shutdown /r /t 1")

    elif 'quit' in query or 'exit' in query:
        speak('Goodbye!')
        exit()
