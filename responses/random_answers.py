

import random

greetings = ['hola','hello','hi','Hi','hey!','hey']

random_greeting = random.choice(greetings)

question = ['how are you ?','ow are you doing ?']
responses = ['I am fine and you ?','well done thanks']
question = ['okay, what is the plan today ?','ow are you doing ?']
responses = ['I am fine and you ?','well done thanks']


random_response = random.choice(responses)


while True:
    userInput = input(">>")
    if userInput in greetings:
        print(random_greeting)
    elif userInput in question:
        print(random_response)
    else:
        print("I did not understand what you said")