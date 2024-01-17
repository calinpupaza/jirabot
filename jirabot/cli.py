import argparse
from dotenv import load_dotenv
from brains.chatbot import setup_jira_agent

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description='JiraBot CLI')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    args = parser.parse_args()

    agent = setup_jira_agent(True)

    print("Enter multiple lines of text (press Ctrl+D to finish):")
    while True:
        try:
            line = input("> ")
            response = agent.run(line)
            print(response)
        except KeyboardInterrupt:
            break
    print()
    print("Goodbye!")

if __name__ == '__main__':
    main()
