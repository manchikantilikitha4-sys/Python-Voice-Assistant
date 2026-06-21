import pyttsx3
import webbrowser
import datetime
import os
import platform
import socket
import requests
import wikipedia
import pyjokes
import psutil
import pywhatkit
import wolframalpha

from openai import OpenAI

# ===================================
# API KEYS
# ===================================

OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"
WOLFRAM_APP_ID = "YOUR_WOLFRAM_APP_ID"

client = OpenAI(api_key=OPENAI_API_KEY)
wolf = wolframalpha.Client(WOLFRAM_APP_ID)

# ===================================
# TEXT TO SPEECH
# ===================================

engine = pyttsx3.init()
engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# ===================================
# USER INPUT
# ===================================

def listen():
    return input("You : ").lower()


# ===================================
# GREETING
# ===================================

def greet():

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning!")

    elif hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your Smart Voice Assistant.")
    speak("How can I help you today?")

    # ===================================
# TIME
# ===================================

def tell_time():
    current = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current}")


# ===================================
# DATE
# ===================================

def tell_date():
    today = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {today}")


# ===================================
# DAY
# ===================================

def tell_day():
    day = datetime.datetime.now().strftime("%A")
    speak(f"Today is {day}")


# ===================================
# OPEN WEBSITES
# ===================================

def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def open_github():
    speak("Opening GitHub")
    webbrowser.open("https://github.com")

def open_linkedin():
    speak("Opening LinkedIn")
    webbrowser.open("https://www.linkedin.com")

def open_maps():
    speak("Opening Google Maps")
    webbrowser.open("https://maps.google.com")


def open_chatgpt():
    speak("Opening ChatGPT")
    webbrowser.open("https://chat.openai.com")

    # ===================================
# WEATHER
# ===================================

def weather():
    city = input("Enter city name: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]

            speak(f"The temperature in {city} is {temp} degree Celsius.")
            speak(f"The weather is {desc}.")

        else:
            speak("City not found.")

    except:
        speak("Unable to fetch weather.")

        # ===================================
# OPENAI CHAT
# ===================================

def ai_chat():

    question = input("Ask AI: ")

    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": question}
            ]
        )

        answer = response.choices[0].message.content

        print(answer)

        speak(answer)

    except Exception as e:
        print(e)
        speak("OpenAI is not configured correctly.")


# ===================================
# WOLFRAM ALPHA CALCULATOR
# ===================================

def calculate():

    question = input("Enter calculation: ")

    try:

        answer = next(wolf.query(question).results).text

        print(answer)

        speak(answer)

    except:
        speak("Sorry, I couldn't calculate.")


# ===================================
# REMINDER
# ===================================

def add_reminder():

    reminder = input("Enter reminder: ")

    with open("reminders.txt", "a") as file:
        file.write(reminder + "\n")

    speak("Reminder saved successfully.")


def show_reminders():

    try:

        with open("reminders.txt", "r") as file:

            data = file.read()

            if data.strip() == "":
                speak("No reminders available.")

            else:
                print(data)
                speak(data)

    except FileNotFoundError:
        speak("Reminder file not found.")


# ===================================
# HELP MENU
# ===================================

def help_menu():

    print("""
========= AVAILABLE COMMANDS =========

time
date
day
google
youtube
gmail
github
linkedin
maps
chatgpt

google search
youtube search
wikipedia

weather
calculate
ai

joke
battery
system
internet

notepad
calculator
paint
cmd
vs code

add reminder
show reminders


    speak("Displayed all available commands.")
    
# ===================================
# BATTERY
# ===================================


help
exit

======================================
     """)

    speak("Displayed all available commands.")
   
    def battery():
     battery_info = psutil.sensors_battery()

    if battery_info is None:
        speak("Battery information is not available.")
        return

    percent = battery_info.percent

    if battery_info.power_plugged:
        speak(f"Battery is {percent} percent and charging.")
    else:
        speak(f"Battery is {percent} percent.")

    # ===================================
# MAIN PROGRAM
# ===================================

def main():

    greet()

    while True:

        command = listen()

        if command == "":
            continue

        # Time & Date
        elif "time" in command:
            tell_time()

        elif "date" in command:
            tell_date()

        elif "day" in command:
            tell_day()

        elif "google" in command:
            open_google()

        elif "youtube" in command:
            open_youtube()

        elif "github" in command:
             open_github()

        elif "linkedin" in command:
          open_linkedin()

        elif "maps" in command:
           open_maps()

        elif "chatgpt" in command:
          open_chatgpt()

        elif "google search" in command:
          google_search()

        elif "youtube search" in command:
          youtube_search()

        elif "wikipedia" in command:
         wiki_search()

        # Smart Features
        elif "weather" in command:
            weather()

        elif "calculate" in command:
            calculate()

        elif command == "ai":
            ai_chat()

        elif "joke" in command:
            tell_joke()

        elif "battery" in command:
            battery()

        elif "system" in command:
            system_info()

        elif "internet" in command:
            internet_status()

        elif "whatsapp" in command:
            whatsapp_message()

        # Applications
        elif "notepad" in command:
            open_notepad()

        elif "calculator" in command:
            open_calculator()

        elif "paint" in command:
            open_paint()

        elif "cmd" in command or "command prompt" in command:
            open_cmd()

        elif "vs code" in command:
            open_vscode()

        # Reminders
        elif "add reminder" in command:
            add_reminder()

        elif "show reminders" in command:
            show_reminders()

        # Help
        elif "help" in command:
            help_menu()

        # Exit
        elif "exit" in command or "quit" in command:
            speak("Thank you. Goodbye!")
            break

        else:
            speak("Sorry, I didn't understand that command.")


if __name__ == "__main__":
    main()