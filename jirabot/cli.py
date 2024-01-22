
from dotenv import load_dotenv
from brains.jiraagent import JiraAgent

load_dotenv()

def main():
    agent = JiraAgent(verbose=True)

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
