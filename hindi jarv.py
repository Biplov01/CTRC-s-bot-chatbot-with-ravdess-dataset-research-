import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Assuming voices[1] is Hindi voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("सुप्रभात!")

    elif 12 <= hour < 18:
        speak("शुभ अपराह्न!")   

    else:
        speak("शुभ संध्या!")  

    speak("मैं जार्विस हूँ। कृपया बताएं कि मैं आपकी कैसे सहायता कर सकता हूँ।")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("सुन रहा हूँ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("जारी है...")    
        query = r.recognize_google(audio, language='hi-IN')  # Recognize in Hindi
        print(f"उपयोगकर्ता ने कहा: {query}\n")

    except Exception as e:
        print(e)    
        print("कृपया फिर से बोलें...")  
        return "None"
    return query

def playMusic():
    music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[0]))

def tellTime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f"सर, वक्त है {strTime}")

def openCode():
    codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def main():
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('विकिपीडिया पर खोज रहा हूँ...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("विकिपीडिया के अनुसार")
            print(results)
            speak(results)

        elif 'यूट्यूब खोलो' in query:
            webbrowser.open("youtube.com")

        elif 'गूगल खोलो' in query:
            webbrowser.open("google.com")

        elif 'स्टैक ओवरफ्लो खोलो' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'म्यूजिक बजाओ' in query:
            playMusic()

        elif 'कहा: भान' in query:
            tellTime()

        elif 'कोड खोलो' in query:
            openCode()

        elif 'हैरी को ईमेल भेजें' in query:
            try:
                speak("क्या कहूं?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("ईमेल भेज दिया गया है!")
            except Exception as e:
                print(e)
                speak("माफ़ करें, मेरे दोस्त हैरी भाई। मुझे इस ईमेल को भेजने में समर्थ नहीं हूँ")    

if __name__ == "__main__":
    main()
