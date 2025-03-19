# speech recognition # wikipedia (to collect data from the wikipedia )
#openai (ai company have gpt4, have api jinke through ham ye sab kaam kar sakte hai)
# pyaudio
from time import strftime


import speech_recognition as sr
import os
import platform
import webbrowser
import datetime
from config import apikey
from mistralai import Mistral


def ai(query):
    api_key = apikey
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": query,
            },
        ]
    )


    print(chat_response.choices[0].message.content)


def say(text):
    if platform.system() == "Windows":
        # Replace single quotes with double quotes to avoid PowerShell issues
        text = text.replace("'", '"')

        # Execute PowerShell TTS command once
        os.system(
            f'powershell -c "Add-Type –AssemblyName System.speech; '
            f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
            f'$speak.Speak(\\"{text}\\");"'
        )


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #Adjusting for ambient noise...
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise

        print("Listening...")
        try:
            audio = r.listen(source, timeout=20, phrase_time_limit=2 6)  # Increase timeout
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except Exception as e:
            pass


if __name__ == '__main__':
    print('Starting System')
    say("Startig System")
    say("Now am ready to take any commands")
    print("Now am ready to take any commands")

    while True:

        text = takeCommand()

        executed = False

        sites = [["youtube","https://www.youtube.com/"],["wikipedia","https://www.wikipedia.org"],["google","https://www.google.com"]]
        for site in sites:
            if text and f"open {site[0]}".lower() in text.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
            break
            executed = True


        try:
            if any(phrase.lower() in text for phrase in ["Hello", "Hi", "Whatsapp","What are you doing"]):
                print("Hi! I'm your coding assistant, crafted by Aayush Gupta. Let's dive into coding or chat about anything!")
                say("Hi! I'm your coding assistant, crafted by Aayush Gupta. Let's dive into coding or chat about anything!")

                executed = True

        except Exception as e:
            pass



        if "the time".lower() in text:
            h = datetime.datetime.now().strftime("%H")
            m = datetime.datetime.now().strftime("%M")
            print(f"Sir, the time is {h} : {m}")
            say(f"Sir, the time is {h} and {m}")

        elif any(phrase in text for phrase in ["explain me", "what is", "where is", "how to"]):
            say("coming back with your result, just 1 second")
            query = text +"Explain this as simply and short as possible, do add EMOJIS wherever it is possible"
            ai(query)
            executed = True

        elif any(phrase in text for phrase in ["Contrast", "Evaluate", "Examine", "Analyze", "Match","compare"]):
            say("just 1 second, Let me look for it in my Database")
            query = text +"Explain this as simply as possible, with comparisons for easy differentiation wherever it is possible, try to add little bit of emojis for user friendly output and do suggest the better option for wide variety of uses"
            ai(query)
            executed = True

        try:
            if any(phrase.lower() in text.lower() for phrase in ["Application","Letters", "email", "Papers", "Research", "Notices", "Essay"]):
                say("Ok, Just one second")
                query = text + " in as simple as possible and in formal tone"
                ai(query)
                executed = True

            elif any(phrase.lower() in text.lower() for phrase in ["code","program", "write a program", "write a code", "java", "c plus plus", "python","javascript"]):
                print("Please specify the programming language")
                say("Please specify the programming language")

                lang = takeCommand()

                print("Oh, That's Easy")
                say("Oh, That's Easy")
                say("Count 5, I'll be back with the perfectly executable code,")
                query = f"{lang} {text}+write only the code, with little bit of explanation not more than 8 words in commented format"
                executed = True
                ai(query)
        except Exception as e:
            pass



        if any(phrase in text for phrase in ["thank", "thanks", "thank you","thanks a lot"]):
            print("Its my pleasure")
            say("Its my pleasure")
            executed = True
            exit()
