from responses import AbstractResponse


class DefaultResponse(AbstractResponse):

    def run(self, command):
        return "Not sure what you mean by {command}. \n" \
               "but d'ont worry i'm here to help you\n" \
               "*Try* somethings like this :\n" \
               "--*hello*, *hi*...\n" \
               "--*i want to* book train ....\n" \
               "--*i want to* visit....\n" \
               "--*i look for* .....\n" \
               "--*do* or something\n" \
               "--*if you have more questions just let me know :)*\n" \
               "--*enjoy your stay*\n".format(
                command=command
        )
