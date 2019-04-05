import random
def farewell ():
    def bye():
        sentence = input()
        FAREWELL_KEYWORDS = ("bye", "goodbye", "farewell", "see you", "see ya")
        FAREWELL_RESPONSES = ["peace","farewell earthling", "bye", "☌⍜⍜⎅⏚⊬⟒"]
        if sentence in FAREWELL_KEYWORDS:
            print(random.choice(FAREWELL_RESPONSES))
    bye()
farewell()
input()
