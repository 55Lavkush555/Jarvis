from pyttsx3 import *
import speech_recognition as sr
import wikipedia
import webbrowser
import os


recognizer = sr.Recognizer()

def takeCommand(c):
    if  'open youtube' in c:
        webbrowser.open('youtube.com')
        print('YouTube is opend.')
        speak('YouTube is opend.')

    elif  'open google' in c:
        webbrowser.open('google.com')
        print('Google is opend.')
        speak('Google is opend.')

    elif  'open chat gpt' in c:
        webbrowser.open('chatgpt.com')
        print('Chat GPT is opend.')
        speak('Chat GPT is opend.')

    elif  'open stackoverflow' in c:
        webbrowser.open('https://stackoverflow.com/')
        print('stackoverflow is opend.')
        speak('stackoverflow is opend.')

    elif  'open replit' in c:
        webbrowser.open('https://replit.com/')
        print('stackoverflow is opend.')
        speak('stackoverflow is opend.')

    elif  '.org' in c:
        webbrowser.open(c)
        print(f'{c} is opend.')
        speak(f'{c} is opend.')

    elif  '.com' in c:
        webbrowser.open(c)
        print(f'{c} is opend.')
        speak(f'{c} is opend.')

    elif  '.in' in c:
        webbrowser.open(c)
        print(f'{c} is opend.')
        speak(f'{c} is opend.')

    elif  'open vs code' in c:
        print('Opening VS code.')
        speak('Opening VS code.')
        os.startfile('c:\\Users\\Lavkush\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk')

    elif  'open browser' in c:
        print('Opening Browser')
        speak('Opening Browser')
        os.startfile('c:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk')

    elif  'quit' in c:
        print('Quitting...')
        speak('quitting')
        quit()

    elif 'are you' in c:
        print('I am Jarvis.\n')
        speak('I am Jarvis')

    else:
        try:
            print('According to wikipedia...\n')
            speak('According to wikipedia')
            print(f'{wikipedia.summary(c, sentences=5)}\n')
            speak(wikipedia.summary(c, sentences=5))

        except:
            print('Nothing found in wikipedia')
            speak('Nothing found in wikipedia')


if __name__ == '__main__':
    print('Hello! Lavkush')
    speak('Hello Lavkush')

    while True:
        
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print('Speak the task\n')
            speak('speak the task')

            audio_data = recognizer.listen(source)

            print("Recognizing speech...")

            try:
    
                text : str = recognizer.recognize_google(audio_data)
                print("You said:\n" + text)
                print(' ')
                
                command = text.lower()
        
                takeCommand(command)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio\n")
                speak("Google Speech Recognition could not understand the audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                speak(f"Could not request results from Google Speech Recognition service; {e}")

                while True:
                    speak('write the input')

                    command = input('Write the task.\n').lower()
                    print(' ')

                    takeCommand(command)