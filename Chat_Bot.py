import random
def Greeting ():
    def greetkey():
        sentence = input("Greeting You Must Enter: ")
        GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up")
        GREETING_RESPONSES = ["take me to your leader","greetings earthling", "Nano Nano", "⊑⟒⌰⌰⍜"]
        if sentence in GREETING_KEYWORDS:
            print(random.choice(GREETING_RESPONSES))
    greetkey()

Greeting()

input()
