import pyttsx3
friend =  pyttsx3.init()
speech = input("Say something : ")
friend.say(speech)
friend.runAndWait()