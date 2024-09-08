6import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from requests import get
from datetime import date

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        print('Recognizing...')
        command = r.recognize_google(audio, language='en-in')
        print(f"User Said : {command}")

    except Exception as e:
        return "none"
    return command


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning, Boss")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, Boss")
    else:
        speak("Good evening Boss")
    speak('I am Friday, How May I Help You')


if __name__ == "__main__":
    wish()
    while True:

        command = takecommand().lower()

        if 'play' in command:
            song = command.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
            print(song)


        elif 'search about' in command:
            ser = command.replace('search about', '')
            speak('Ok Boss, I am searching')
            pywhatkit.search(ser)


        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H %M %p')
            speak('Right Now time is ' + time)


        elif 'tell me about' in command:
            person = command.replace('tell me about', '')
            try:
                info = wikipedia.summary(person, 2)
                speak(info)
            except Exception:
                speak("Could you be more specific")


        elif 'repeat' in command:
            acr = command.replace('repeat', '')
            speak(acr)


        elif 'joke' in command:
            speak(pyjokes.get_joke())

        elif 'how are' in command:
            speak('''I'm great, thanks to your quick system and fast internet access, and what about you, boss?''')
            har = takecommand().lower()
            if 'fine' in har:
                speak('''That's something I'd like to hear more of. I just want to know if you want to do something, please let me know.''')
            elif 'sad' in har:
                speak('I can tell you a joke to make you feel better')
                speak(pyjokes.get_joke())



        elif 'open youtube' in command:
            speak('Ok Boss')
            webbrowser.open("youtube.com")


        elif 'open google' in command:
            speak('Ok Boss')
            speak('Hey Boss, What should I search')
            ab = takecommand().lower()
            webbrowser.open(f"{ab}")


        elif 'open sublime' in command:
            speak('Ok Boss')
            codepath = "C:\\Program Files\\Sublime Text\\sublime_text.exe"
            os.startfile(codepath)

        elif 'open minecraft' in command:
            speak('Ok Boss')
            codepath = "C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe"
            os.startfile(codepath)

        elif 'open notepad' in command:
            speak('Ok Boss')
            codepath = "%windir%\\system32\\notepad.exe"
            os.startfile(codepath)

        elif 'take note' in command:
            speak('Ok Boss')
            speak('Boss, What do you want to write')
            f = open("Notes.txt", "a")
            time = datetime.datetime.now().strftime('\n\n%H %M %p')
            f.write(time)
            today = date.today()
            d1 = today.strftime("\n%d/%m/%Y\n")
            f.write(d1)
            tfc = takecommand().lower()
            f.write(tfc)
            f.close()
            speak('Boss I have written it down in a text file.')

        elif 'ip address' in command:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")


        elif 'cut the power' in command:
            speak('Bye Bye Boss')
            exit()

        elif 'shutdown' in command:
            speak('Bye Bye Boss')
            exit()

        else:
            speak('Say that again, I cant get it')
