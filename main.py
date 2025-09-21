from speech_module import wishMe, takeCommand, speak
from task_module import perform_task

if __name__ == "__main__":
    wishMe()
    last_query = ""
    while True:
        query = takeCommand().lower() 
        if query != "none":
            last_query = query
            perform_task(query)


        
        if "how are you" in query or "how r u" in query:
            print("I'm just a program, but I'm functioning well. Thank you for asking!")
            speak("I'm just a program, but I'm functioning well. Thank you for asking!")
        
        elif "help" in query:
            print("You can ask me to open websites, tell you the time, create or delete files, and more.")
            speak("You can ask me to open websites, tell you the time, create or delete files, and more.")
        
        elif "was that helpful" in query:
            speak("I hope it was! Let me know if you need more assistance.")
        
        elif "love you" in query or "love u" in query:
            print("I am just a Program   :( ")
            speak("I am just a program, and please don't think about that...")
        
        elif "what's your name" in query or "who are you" in query:
            print("I am your voice assistant, here to help you!")
            speak("I am your voice assistant, here to help you!")

        elif "your name" in query or "what is your name" in query:
            print("I am just a Program I don't have a name")
            speak("I am just a Program. I don't have a name")