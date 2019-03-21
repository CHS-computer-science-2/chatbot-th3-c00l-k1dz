def Greeting ():
    def check_for_greeting(sentence):
        for word in sentence.words:
            if word.lower() in GREETING_KEYWORDS:
                print(GREETING_RESPONSES)
                return random.choice(GREETING_RESPONSES)
    def greetkey():    
        sentence= str(input("Greeting You Must Enter: "))
        GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up")
        GREETING_RESPONSES = ["*Vulcan Salute*", "take me to your leader","greetings earthling", "Nano Nano", "⊑⟒⌰⌰⍜"]
        print(check_for_greeting(sentence))
    greetkey()
    
Greeting()

