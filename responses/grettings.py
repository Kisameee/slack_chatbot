from responses import AbstractResponse
import random

HELLO_COMMAND = "hola David", "hello David", "hi", "Hi David", "hey!", "hey David"
HOW_COMMAND = 'how are you?', 'how are you doing?'
HOW_ANSWERS = 'Okay','I am fine'


class Grettings(AbstractResponse):

    def run(self, command):
        if command.startswith(HELLO_COMMAND):
            return random.choice(HELLO_COMMAND)
        elif command.startswith(HOW_COMMAND):
            return random.choice(HOW_ANSWERS)
        return None




