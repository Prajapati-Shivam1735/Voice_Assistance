import speech_recignition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    print ("Asistant : ",text)
    engine.say(text)
    engine.runAndWait()

# unction to listen to user commands
def listen():
    with sr.Microphone() as source:
        print("Listening.......")
        recognizer.adjust_for_ambitient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""
# Function to process commands
def process_command(command):
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you today?")

    elif "time" in command:
        currrent_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {currrent_time}")
    
    elif " date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        speak("What would you like me to search for?")
        query = listen()
        if query:
            speak(f"Searching the wrb for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day!" )
        exit()
    else:
        speak("I'm not sure how to help with that yet.")

def run_assistant():
    speak("Voice assistant activated. Say something!")
    while True:
        command = listen()
        if command:
            process_command(command)
if __name__== "__main__":
    run_assistant()