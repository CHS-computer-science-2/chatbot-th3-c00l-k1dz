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

def main():
    GREETING_RESPONSES = ["take me to your leader","greetings earthling", "Nano Nano", "⊑⟒⌰⌰⍜"]
    FAREWELL_RESPONSES = ["peace","farewell earthling", "bye", "☌⍜⍜⎅⏚⊬⟒"]
    print(random.choice(GREETING_RESPONSES))
    # all checks go here \/
    x=0
    while x==0:
        input("Type here you must: ")

main()
