import argparse

from selenium import webdriver


def parse_args():
    parser = argparse.ArgumentParser(description="Selenium")

    # Positional argument for the URL
    parser.add_argument("url", help="URL to open in the browser")

    # Optional for choose webdriver
    parser.add_argument(
        "-d",
        "--driver",
        default="firefox",
        choices=["firefox", "chrome", "edge"],
        help="webdriver for browser (default: firefox)",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if args.driver == "firefox":
        driver = webdriver.Firefox()
    elif args.driver == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("unsupported WebDriver")

    # Open the provided URL
    driver.get(args.url)

    input("Pres Enter to close the browser...")
    driver.quit()
