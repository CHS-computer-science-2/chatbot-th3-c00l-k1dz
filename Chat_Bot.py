import random

def greeting(sentence):
    GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up")
    GREETING_RESPONSES = ["take me to your leader","greetings earthling", "Nano Nano", "⊑⟒⌰⌰⍜"]
    if sentence in GREETING_KEYWORDS:
        print(random.choice(GREETING_RESPONSES))
    return

def farewell(sentence):
    FAREWELL_KEYWORDS = ("bye", "goodbye", "farewell", "see you", "see ya")
    FAREWELL_RESPONSES = ["peace","farewell earthling", "bye", "☌⍜⍜⎅⏚⊬⟒"]
    if sentence in FAREWELL_KEYWORDS:
        print(random.choice(FAREWELL_RESPONSES))
    return

def main():
    GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up")
    FAREWELL_KEYWORDS = ("bye", "goodbye", "farewell", "see you", "see ya")
    # all checks go here \/
    x=0
    while x==0:
        word = input("Type here you must: ")
        if word in GREETING_KEYWORDS:
            greeting(word)
        elif word in FAREWELL_KEYWORDS:
            farewell(word)

main()
