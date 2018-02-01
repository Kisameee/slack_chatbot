import re

import googlesearch

from responses import AbstractResponse

SEARCH_COMMAND = re.compile('i want to visit\s+(?P<place>.+)\s*', re.IGNORECASE)


class SearchPlaceResponse(AbstractResponse):

    def run(self, command):
        command_search = SEARCH_COMMAND.search(command)
        if command_search is not None:
            place = command_search.group('place')
            response = googlesearch.search(
                'Visiting ' + place,
                lang="en",
                num=1,
                stop=1,
                pause=1
            )
            result_list = [i for i in response]
            return '\n'.join(['Yeah, you\'re right ... {place} is a nice place !'.format(place=place)] + result_list)
        return None
