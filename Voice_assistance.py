import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sounddevice as sd
import numpy as np

# Initialize text-to-speech
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    """Make the assistant speak."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Record audio using sounddevice (no PyAudio needed)."""
    speak("Listening...")
    duration = 4  # seconds
    sample_rate = 44100
    try:
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()  # Wait for recording to finish
        audio_data = sr.AudioData(recording.tobytes(), sample_rate, 2)
        command = recognizer.recognize_google(audio_data)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except Exception as e:
        speak(f"An error occurred: {e}")
        return ""

def process_command(command):
    """Handle user commands."""
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you today?")
    
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    
    elif "search" in command:
        speak("What would you like me to search for?")
        query = listen()
        if query:
            speak(f"Searching the web for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
    
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day!")
        exit()
    
    else:
        speak("I'm not sure how to help with that yet.")

def run_assistant():
    """Main loop."""
    speak("Voice assistant activated. Say something!")
    while True:
        command = input("You: ")
        if command:
            process_command(command)

if __name__ == "__main__":
    run_assistant()
