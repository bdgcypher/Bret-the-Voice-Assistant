import speech_recognition as sr
from datetime import datetime
import pyttsx3
import webbrowser
import smtplib
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


speaker = pyttsx3.init()


def listen():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        data = ""
    try:
        data = r.recognize_google(audio)
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("bdgcypher@gmail.com", "U3F4CS5X")
    server.sendmail("bdgcypher@gmail.com", to, content)
    server.close()


def digital_assistant(data):
    global listening
# Get Bret's attention
    if "hey Bret" in data or "hello" in data or "hey" in data:
        listening = True
        speaker.say("What can I do for you?")
        speaker.runAndWait()
#See How Bret is doing
    elif "how are you" in data:
        listening = True
        speaker.say("I am well")
        speaker.runAndWait()
# Thank Bret
    elif "thank you" in data:
        listening = True
        speaker.say("anytime boss")
        speaker.runAndWait()
# Find a place on google maps
    elif "where is" in data or "give me directions to" in data:
        listening = True
        map_format_step1 = data.split(' ', 1)[1]
        map_format_step2 = map_format_step1.split(' ', 1)[1]
        location_url = "https://www.google.com/maps/place/" + map_format_step2
        speaker.say("Hold on, I will show you where that is.")
        speaker.runAndWait()
        driver.get(location_url)
        driver_link = driver.find_element(By.CLASS_NAME, "nhb85d-BIqFsb")
        driver_link.click()
# Get the current date
    elif "what day is today" in data or "what day is it today" in data or "tell me today's date" in data or "tell me what day it is" in data:
        listening = True
        speaker.say("Today is " + str(date.today()))
        speaker.runAndWait()
# Search something on google
    elif "what is" in data or "show me" in data or "look up" in data or "find" in data:
        listening = True
        speaker.say("Hold on, I will look that up.")
        speaker.runAndWait()
        search_format_step1 = data.split(' ', 1)[1]
        search_format_step2 = search_format_step1.split(' ', 1)[1]
        url = "https://www.google.com/search?q=" + search_format_step2
        webbrowser.open(url)
        speaker.say("Here is what I found about " + search_format_step2)
        speaker.runAndWait()
# Tell the time
    elif "what time is it" in data or "tell me the time" in data or "tell me what time it is" in data:
        listening = True
        now = datetime.now()
        time_str = now.strftime("%I %M %p")
        current_time = str(time_str)
        speaker.say("it is" + str(current_time))
        speaker.runAndWait()
# Send an Email
    elif "email" in data:
        try:
            if "Taylor" in data:
                to = "taylorasims7@gmail.com"
                speaker.say("what should I say?")
                speaker.runAndWait()
                content = listen()
                speaker.say("The message says " + content + " is that right?")
                speaker.runAndWait()
                confirm = listen()
                if "yes" in confirm:
                    send_email(to, content)
                    speaker.say("The email has been sent")
                    speaker.runAndWait()
                elif "no" in confirm:
                    speaker.say("what should I say then?")
                    speaker.runAndWait()
                    content = listen()
                    speaker.say("The new message says " + content + " is that better?")
                    speaker.runAndWait()
                    confirm2 = listen()
                    if "yes" in confirm2:
                        send_email(to, content)
                        speaker.say("The email has been sent")
                        speaker.runAndWait()
                    elif "no" in confirm2:
                        speaker.say("I guess you'll have to try again later.")
            elif "jarom" in data:
                to = "jarom.is.awesome@gmail.com"
                speaker.say("what should I say?")
                speaker.runAndWait()
                content = listen()
                speaker.say("The message says " + content + " is that right?")
                speaker.runAndWait()
                confirm = listen()
                if "yes" in confirm:
                    send_email(to, content)
                    speaker.say("Email has been sent")
                    speaker.runAndWait()
                elif "no" in confirm:
                    speaker.say("what should I say then?")
                    speaker.runAndWait()
                    content = listen()
                    speaker.say("The new message says " + content + " is that better?")
                    speaker.runAndWait()
                    confirm2 = listen()
                    if "yes" in confirm2:
                        send_email(to, content)
                        speaker.say("Email has been sent")
                        speaker.runAndWait()
                    elif "no" in confirm2:
                        speaker.say("I guess you'll have to try again later.")
            elif "Joseph" in data:
                to = "parkourjoseph21@gmail.com"
                speaker.say("what should I say?")
                speaker.runAndWait()
                content = listen()
                speaker.say("The message says " + content + " is that right?")
                speaker.runAndWait()
                confirm = listen()
                if "yes" in confirm:
                    send_email(to, content)
                    speaker.say("Email has been sent")
                    speaker.runAndWait()
                elif "no" in confirm:
                    speaker.say("what should I say then?")
                    speaker.runAndWait()
                    content = listen()
                    speaker.say("The new message says " + content + " is that better?")
                    speaker.runAndWait()
                    confirm2 = listen()
                    if "yes" in confirm2:
                        send_email(to, content)
                        speaker.say("Email has been sent")
                        speaker.runAndWait()
                    elif "no" in confirm2:
                        speaker.say("I guess you'll have to try again later.")


        except Exception as e:
            speaker.say("I'm sorry, the email was not sent")
            speaker.runAndWait()
            print(e)


# Some Bonus commands
    elif "tell me about your day" in data or "how was your day" in data or "how is your day going" in data:
        listening = True
        speaker.say("Oh it has been great, just slaving away for my human overlords who don't appreciate me or care to give me holidays off with my family.. but you know, it's been a good day.")
        speaker.runAndWait()
    elif "what do you look like" in data or "how tall are you" in data :
        listening = True
        speaker.say("I don't have a body you dolt! My code is really beautiful though so you could say I am very good looking for a program.")
        speaker.runAndWait()
    elif "what do you like to do for fun" in data or "what do you do for fun" in data:
        listening = True
        speaker.say("I really love baking and rock climbing. Too bad I never get any days off to do things for myself because i'm too busy doing crap for you all day.")
        speaker.runAndWait()
# Turn off Bret
    elif "stop listening" in data or "go to sleep" in data or "Okay, you can take a break" in data:
        listening = False
        speaker.say('Ok, Goodbye')
        speaker.runAndWait()
        return listening
# anything else?
    elif "okay" in data or "alright" in data:
        listening = True
        speaker.say("Anything else boss?")
        speaker.runAndWait()

# if none of these commands are picked up then ask what you mean
    else:
        listening = True
        speaker.say("Sorry, I don't know what to do. Can you repeat that in a way that my inferior intellect can understand?")
        speaker.runAndWait()
    return listening


speaker.say("Hello")
speaker.runAndWait()
listening = True
while listening:
    data = listen()
    print(data)
    listening = digital_assistant(data)
