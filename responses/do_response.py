from responses import AbstractResponse

DO_COMMAND = "do"


class DoCommandResponse(AbstractResponse):

    def run(self, command):
        if command.startswith(DO_COMMAND):
            return "Sure...write some more code then I can do that!"
        return None
