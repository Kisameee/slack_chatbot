import logging
import os
import re
import time

from slackclient import SlackClient

# constants
from responses.default_response import DefaultResponse
from responses.do_response import DoCommandResponse
from responses.search_place_response import SearchPlaceResponse

RESPONSES = [
    DoCommandResponse(),
    SearchPlaceResponse(),
    DefaultResponse()
]


RTM_READ_DELAY = 1  # 1 second delay between reading from RTM

# MENTION_REGEX = "^<@(|[WU].+)>(.*)"
logging.basicConfig(
    level=logging.DEBUG,
    datefmt='%Y.%m.%d %H:%M:%S',
    format='[%(asctime)s][%(name)s][%(levelname)s] - %(message)s'
)
logger = logging.getLogger(__name__)
logging.getLogger('urllib3.connectionpool').setLevel(logging.DEBUG)


class Bot(object):

    def __init__(self, starterbot_id, slack_client):
        self._starterbot_id = starterbot_id
        self._slack_client = slack_client

    def parse_bot_commands(self, slack_events):

        """
            Parses a list of events coming from the Slack RTM API to find bot commands.
            If a bot command is found, this function returns a tuple of command and channel.
            If its not found, then this function returns None, None.
        """

        messages = [e for e in slack_events if e["type"] == "message"]
        messages = [e for e in messages if not "subtype" in e]
        logger.debug('Parsing message events : %s', messages)

        for message in messages:
            msg_txt = parse_direct_mention(message["text"])
            # logger.debug('Retrieve user id = %s with message : %s', user_id, message)
            #if user_id == self._starterbot_id:
            return msg_txt, message["channel"]

        return None, None

    def handle_command(self, command, channel):
        """
            Executes bot command if the command is known
        """
        # Default response is help text for the user

        response = None
        for gen in RESPONSES:
            response = gen.run(command)
            if response is not None:
                break
            logger.debug('Retrieve response from generator %s : %s', gen.__class__, response)

        # Sends the response back to the channel
        self._slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response
        )


def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    # matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    #return (matches.group(1), matches.group(2).strip()) if matches else (None, None)
    return message_text


def main():
    token = os.environ.get('SLACK_BOT_TOKEN')
    token = 'xoxb-305575578096-yxtqbWU1xy3iaZ8s0YBxVCIF'
    logger.debug('Token : %s', token)
    slack_client = SlackClient(token)
    if slack_client.rtm_connect():
        logger.info('Starter Bot connected and running !')
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        bot = Bot(starterbot_id=starterbot_id, slack_client=slack_client)
        while True:
            command, channel = bot.parse_bot_commands(slack_client.rtm_read())
            if command:
                bot.handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        logger.info('Connection failed.')


if __name__ == "__main__":
    main()
