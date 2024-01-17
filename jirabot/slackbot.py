import os
from dotenv import load_dotenv
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from brains.chatbot import setup_jira_agent
from brains.message_queue import event_queued_or_recent, enqueue_event

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
    event_id = event_data["event_id"]
    if event_queued_or_recent(event_id):
        pass
    enqueue_event(event_id)
    message = event_data["event"]
    channel_id = message["channel"]
    user_id = message.get("user")
    text = message.get("text")
    bot_id = message.get("bot_id")
    if bot_id is None:
        try:
            response = agent.run(text)
            slack_client.chat_postMessage(channel=channel_id, text=response)
        except Exception as e:
            try:
                error_message = "An error occurred. Details: " + str(e)
                slack_client.chat_postMessage(channel=channel_id, text=error_message)
            except:
                return

    return

# Start the event listener
slack_events_adapter.start(port=3000)
