import re

class IntentParser:
    def __init__(self):
        self.intent_patterns = {
            "greeting": [
                r"\b(hi|hello|hey)\b",                      # English
                r"\b(здраво|поздрав|ајде)\b",               # Macedonian
                r"\b(zdravo|pozdrav|ćao|hej)\b"             # Serbian
            ],
            "goodbye": [
                r"\b(bye|goodbye|see you)\b",
                r"\b(чао|довиђење|се гледаме)\b",
                r"\b(ćao|doviđenja|vidimo se)\b"
            ],
            "thanks": [
                r"\b(thanks|thank you)\b",
                r"\b(благодарам|фала)\b",
                r"\b(hvala|zahvaljujem)\b"
            ],
            "weather": [
                r"\b(weather|rain|sunny|forecast)\b",
                r"\b(време|дожд|сонце|прогноза)\b",
                r"\b(vreme|kiša|sunce|prognoza)\b"
            ],
            "news": [
                r"\b(news|headlines|updates)\b",
                r"\b(вести|новости|информации)\b",
                r"\b(vesti|novosti|informacije)\b"
            ],
            "joke": [
                r"\b(joke|funny|laugh)\b",
                r"\b(виц|смешно|се смеам)\b",
                r"\b(vic|smešno|smeh)\b"
            ],
            "name": [
                r"\b(name|who are you)\b",
                r"\b(име|кој си ти)\b",
                r"\b(ime|ko si ti)\b"
            ],
            "age": [
                r"\b(age|how old)\b",
                r"\b(години|колку години)\b",
                r"\b(godine|koliko godina)\b"
            ],
            "help": [
                r"\b(help|support|assist)\b",
                r"\b(помош|поддршка|асистенција)\b",
                r"\b(pomoć|podrška|asistencija)\b"
            ]
        }

    def parse_intent(self, user_input: str) -> str:
        user_input = user_input.lower()
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if re.search(pattern, user_input):
                    return intent
        return "unknown"

# Пример
if __name__ == "__main__":
    parser = IntentParser()
    test_inputs = [
        "Здраво пријателе!",
        "Can you help me?",
        "Vidimo se kasnije.",
        "Какво е времето денес?"
    ]
    for text in test_inputs:
        print(f"Input: {text} → Intent: {parser.parse_intent(text)}")
