from typing import Optional
import re

class IntentParser:
    def __init__(self):
        # Клучни зборови за секоја категорија
        self.intent_keywords = {
            "ecology": ["екологија", "одржливост", "рециклирање", "природа", "загадување"],
            "spirituality": ["духовност", "медитација", "свесност", "енергија", "вибрации"],
            "technology": ["технологија", "АИ", "иновации", "дигитално", "машинско учење"],
            "harmony": ["хармонија", "баланс", "усогласеност", "мудрост", "животна средина"]
        }

    def parse_intent(self, text: str) -> Optional[str]:
        text = text.lower()
        for intent, keywords in self.intent_keywords.items():
            for keyword in keywords:
                if re.search(rf"\b{keyword}\b", text):
                    return intent
        return "unknown"

# Пример употреба
if __name__ == "__main__":
    parser = IntentParser()
    sample_text = "Како може АИ да помогне во одржливост и хармонија со природата?"
    intent = parser.parse_intent(sample_text)
    print(f"Препознаена намера: {intent}")
