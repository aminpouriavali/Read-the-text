import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

text = input("Enter a text: ")

engine.say(text)
engine.runAndWait()
