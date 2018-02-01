

import re
import googlesearch
from responses import AbstractResponse

LOOK_COMMAND = re.compile('i want to\s+(?P<things>.+)\s*', re.IGNORECASE)


class Lookfor(AbstractResponse):

    def run(self, command):
        command_search = LOOK_COMMAND.search(command)
        if command_search is not None:
            things = command_search.group('things')
            response = googlesearch.search(
                'paris ' + things,
                lang="en",
                num=1,
                stop=1,
                pause=1
            )
            result_list = [i for i in response]
            return '\n'.join(['that\'s what i find but i need more code to get your location !'.format(things=things)] + result_list)
        return None
