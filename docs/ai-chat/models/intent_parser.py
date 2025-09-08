import re

intents = {
    "greeting": {
        "keywords": [
            "hello", "hi", "hey", "hola",
            "здраво", "поздрав", "ајде",
            "zdravo", "pozdrav", "ćao", "hej"
        ],
        "responses": {
            "en": "Hello! How can I help you?",
            "mk": "Здраво! Како можам да ти помогнам?",
            "sr": "Zdravo! Kako mogu da ti pomognem?"
        }
    },
    "goodbye": {
        "keywords": [
            "bye", "goodbye", "see you", "adios",
            "чао", "довиђење", "се гледаме",
            "ćao", "doviđenja", "vidimo se"
        ],
        "responses": {
            "en": "Goodbye! Have a great day!",
            "mk": "Чао! Имај убав ден!",
            "sr": "Doviđenja! Prijatan dan!"
        }
    },
    "thanks": {
        "keywords": [
            "thanks", "thank you", "gracias",
            "благодарам", "фала",
            "hvala", "zahvaljujem"
        ],
        "responses": {
            "en": "You're welcome!",
            "mk": "Нема на што!",
            "sr": "Nema na čemu!"
        }
    },
    "weather": {
        "keywords": [
            "weather", "rain", "sunny", "forecast",
            "време", "дожд", "сонце", "прогноза",
            "vreme", "kiša", "sunce", "prognoza"
        ],
        "responses": {
            "en": "I'm not sure, but you can check a weather website.",
            "mk": "Не сум сигурен, но можеш да провериш на веб-страница за временска прогноза.",
            "sr": "Nisam siguran, ali možeš da pogledaš vremensku prognozu na nekom sajtu."
        }
    },
    "help": {
        "keywords": [
            "help", "support", "assist",
            "помош", "поддршка", "асистенција",
            "pomoć", "podrška", "asistencija"
        ],
        "responses": {
            "en": "I'm here to assist you. What do you need?",
            "mk": "Тука сум да ти помогнам. Што ти треба?",
            "sr": "Tu sam da ti pomognem. Šta ti treba?"
        }
    },
    "unknown": {
        "keywords": [],
        "responses": {
            "en": "I'm sorry, I didn't understand that.",
            "mk": "Извини, не те разбрав.",
            "sr": "Izvini, nisam razumeo."
        }
    }
}

def parse_intent(text: str, language: str = "en") -> str:
    text = text.lower()
    for intent, data in intents.items():
        for keyword in data["keywords"]:
            if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                return data["responses"].get(language, data["responses"]["en"])
    return intents["unknown"]["responses"].get(language, intents["unknown"]["responses"]["en"])

# Пример за употреба
if __name__ == "__main__":
    print("Type your message (English, Македонски, Srpski):")
    user_input = input("You: ")
    lang_choice = input("Choose language (en/mk/sr): ").strip().lower()
    response = parse_intent(user_input, language=lang_choice)
    print("Bot:", response)
