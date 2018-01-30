from responses import AbstractResponse

EXAMPLE_COMMAND = "do"


class DoCommandResponse(AbstractResponse):

    def run(self, command):
        if command.startswith(EXAMPLE_COMMAND):
            return "Sure...write some more code then I can do that!"
        return None
