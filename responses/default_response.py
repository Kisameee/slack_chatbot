from responses import AbstractResponse


class DefaultResponse(AbstractResponse):

    def run(self, command):
        return "Not sure what you mean by {command}. Try *do* or something like *I want to visit ?*.".format(
            command=command
        )
