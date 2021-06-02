#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from Chatbotv2 import Chatbot

def main():
    # Listen
    zufallsantworten = ["Oh wirklich...",
                        "Interessant",
                        "Das kann man so sehen",
                        "Ich verstehe"]
    reaktionen = {"hallo": "aber Hallo",
                    "geht": "was verstehst du darunter?",
                    "schmeckt": "Ich habe keinen Geschmackssinn."}
    # Ausgabe Begrüßung
    print("Willkommen beim Chatbot(v2)")
    print("Zum beenden geben sie bye ein.")
    print("Worüber wollen Sie sprechen?")

    # Chatbot-Objekt
    bot = Chatbot(reaktionen, zufallsantworten)

    # Logik
    nutzereingabe = ""
    while nutzereingabe != "bye":
        nutzereingabe = ""
        while nutzereingabe == "":
            nutzereingabe = input("Ihre Frage oder Antwort:" )
        if nutzereingabe == "bye":
            break
        bot.set_message(nutzereingabe)
        print(bot.get_response())
    
    # Ausgabe Verabschiedung
    print("Bis zum nächsten mal.")

    main()