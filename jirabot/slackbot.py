import os
from dotenv import load_dotenv
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from brains.jiraagent import JiraAgent

from multiprocessing import Pool

load_dotenv()

# Initialize Slack API client
slack_token = os.environ.get("SLACK_API_TOKEN")
slack_client = WebClient(token=slack_token)

# Initialize Slack event adapter
slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/action")

agent = JiraAgent(False)

# Define event handler for message events
@slack_events_adapter.on("message")
def handle_event(event_data):
    try:
        pool.apply_async(handle_event_impl, (event_data,))
    except Exception as e:
        print(e)
    else:
        print("ACK event " + event_data["event_id"])
    return 

def handle_event_impl(event_data):
    print("handling event " + event_data["event_id"])
    message = event_data["event"]
    channel_id = message["channel"]
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

if __name__ == "__main__":
    pool = Pool()
    # Start the event listener
    slack_events_adapter.start(port=3000)
