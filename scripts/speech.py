# from gtts import gTTS
# def speak(text):                #https://pypi.org/project/gtts/
#     tts = gTTS(text=text, lang='en')
#     tts.save("speech.mp3")
#     import os
#     import playsound
#     playsound.playsound("speech.mp3", True)
#     os.remove("speech.mp3")
#
import pyttsx3                  #https://pypi.org/project/pyttsx3/
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
