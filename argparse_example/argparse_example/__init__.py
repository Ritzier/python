import argparse


def login_qr():
    print("Logging in with QR code...")


def login_code():
    print("Logging in with verification code...")


def login_browser():
    print("Logging in via browser...")


def chat():
    print("Starting chat...")


def ls():
    print("Listing files...")


def parse_args():
    parser = argparse.ArgumentParser(description="Command Line Args")
    subparsers = parser.add_subparsers(
        title="commands", dest="command", metavar="<command>"
    )

    # Subparser for 'login' command
    login_parser = subparsers.add_parser("login", help="Login operations")
    login_parser.add_argument(
        "method", choices=["qr", "code", "browser"], help="Login method"
    )

    # Subparser for 'chat' command
    subparsers.add_parser("chat", help="Start a chat")

    args = parser.parse_args()

    match args.command:
        case "login":
            match args.method:
                case "qr":
                    login_qr()
                case "code":
                    login_code()
                case "browser":
                    login_browser()

        case "chat":
            chat()
        case "ls":
            ls()


def main():
    parse_args()
