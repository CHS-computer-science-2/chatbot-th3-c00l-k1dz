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

def construct_response(sentence):
    resp = ["*nods head*","interstellar", "out of this world", "galatical", "ok"]
    print(random.choice(resp))
    return

def question(sentence):
    quest_resp = ["*sarcasm* "+sentence+" What kind of \nquestion is that ","*nothing*","Answer that I won't",
                  "I didn't travel thousands of \nlight years to answer your silly questions", "Why exactly do you want to know that?","Classified"]
    print(random.choice(quest_resp))
    return

def main():
    GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up")
    FAREWELL_KEYWORDS = ("bye", "goodbye", "farewell", "see you", "see ya")
    verb_list = ['be', 'am', 'is', 'run', 'have', 'do', 'say', 'go', 'get', 'make', 'know', 'think', 'take', 'see', 'come', 'want', 'look',
                 'use', 'find', 'give', 'tell', 'work', 'call', 'try', 'ask', 'need', 'feel', 'become', 'leave', 'put', 'mean', 'keep', 'let',
                 'begin', 'seem', 'help', 'talk', 'turn', 'start', 'show', 'hear', 'play', 'run', 'move', 'like', 'believe', 'hold', 'bring',
                 'happen', 'write', 'provide', 'sit', "I'm"]
    quest_check = ["?", "how", "what", "when", "where", "who", "why"]
    # all checks go here \/
    x=0
    while x==0:
        word = input("Type here you must: ")
        if word in GREETING_KEYWORDS:
            greeting(word)
        elif word in FAREWELL_KEYWORDS:
            farewell(word)
            x += 1
        else:
            for y in quest_check:
                if y in word:
                    question(word)
        for y in verb_list:
            if y in word:
                construct_response(word)

main()
