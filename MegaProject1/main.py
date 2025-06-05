import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
recognizor = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
       speak("Opening Google")
       webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
       speak("Opening YouTube")
       webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
       song = c.lower().split(" ")[1]
       link = musicLibrary.music[song] 
       webbrowser.open(link)

    # Let open ai handle the request
    else: 
       pass

if __name__ == "__main__":
   speak("Initializing Jarvis.....")

   while True:
       
    #Listen for the wake word jarvis
    #obtain audio from the microphone
    r = sr.Recognizer()
    
    print("recognizing...")
    try: 
       with sr.Microphone() as source:
           print("Listening..")
           audio = r.listen(source, timeout=5, phrase_time_limit=1)
       word = r.recognize_google(audio)
       if(word.lower() == "jarvis"):
          speak("yaa")
          # Listen for the command
          with sr.Microphone() as source:
                print("Jarvis active")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)
    
    except Exception as e:
       print("Error; {0}".format(e))   