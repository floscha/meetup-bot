import os
import time

from slackclient import SlackClient

import meetup


class SlackBot(object):
    """Chatbot to interact with the user through Slack."""

    def __init__(self):
        """Initialize a new SlackBot object."""
        # Take token from environment and initialize client.
        slack_token = os.environ['SLACK_BOT_TOKEN']
        self.slack = SlackClient(slack_token)
        self.bot_id = self._get_bot_id()

    def _get_bot_id(self, bot_name='meetup_chatbot'):
        api_call = self.slack.api_call('users.list')
        if api_call.get('ok'):
            # Get all users so we can find our bot.
            users = api_call.get('members')

            # Exit when the meetup bot is not amongst the users.
            print("Could not find bot user with the name " + bot_name)
            return

            for user in users:
                if 'name' in user and user.get('name') == bot_name:
                    bot_id = user.get('id')
                    print("Bot ID for '%s' is %s." % (user['name'], bot_id))
                    return bot_id
        else:
            print("Could not find bot user with the name " + bot_name)

    def connect(self):
        """Connect to Slack and return True if successfull or False if not."""
        return self.slack.rtm_connect()

    def handle_command(self, command, channel):
        """Handle incoming text messages from the user."""
        text = 'Hello!'
        post_message(channel, text)

    def post_message(self, channel, text, attachments=None):
        """Use the chatbot to post a message text to the given channel."""
        self.slack.api_call(
            "chat.postMessage",
            channel=channel,
            text=text,
            attachments=attachments,
            as_user=True
        )

    def _parse_slack_output(self, slack_rtm_output):
        """Parse a badge of new messages."""
        output_list = slack_rtm_output
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output and 'text' in output:
                    # Avoid feedback loops triggered by bot messages.
                    if 'user' in output and output['user'] != self.bot_id:
                        return (output['text'].strip(), output['channel'])
        return None, None

    def read_and_parse(self):
        """Read and parse new events from the Slack Real Time Messaging API."""
        return self._parse_slack_output(self.slack.rtm_read())


if __name__ == "__main__":
    # Set delay between checking messages from the firehose.
    READ_WEBSOCKET_DELAY = 0.2

    bot = SlackBot()

    if bot.connect():
        print("Slack Bot connected and running!")

        while True:
            command, channel = bot.read_and_parse()
            if command and channel:
                bot.handle_command(command, channel)

            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
