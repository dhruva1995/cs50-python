import cowsay
import pyttsx3

engine = pyttsx3.init()
sentence = input("What's the text? ")
cowsay.beavis(sentence)
engine.say(sentence)
engine.runAndWait()
