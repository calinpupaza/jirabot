import argparse

def main():
    parser = argparse.ArgumentParser(description='JiraBot CLI')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')

    args = parser.parse_args()

    print("Enter multiple lines of text (press Ctrl+D to finish):")
    while True:
        try:
            line = input("> ")
            print("...")
        except EOFError:
            break
    print("Goodbye!")

if __name__ == '__main__':
    main()
