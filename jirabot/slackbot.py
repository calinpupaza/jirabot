import os
from dotenv import load_dotenv
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from brains.chatbot import setup_jira_agent

load_dotenv()

# Initialize Slack API client
slack_token = os.environ.get("SLACK_API_TOKEN")
slack_client = WebClient(token=slack_token)

# Initialize Slack event adapter
slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/action")

agent = setup_jira_agent(False)

# Define event handler for message events
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    channel_id = message["channel"]
    user_id = message.get("user")
    text = message.get("text")
    bot_id = message.get("bot_id")
    if bot_id is None:
        response = agent.run(text)
        slack_client.chat_postMessage(channel=channel_id, text=response)

# Start the event listener
slack_events_adapter.start(port=3000)
