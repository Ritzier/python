import argparse

from selenium import webdriver
from selenium.webdriver.common.by import By


def parse_args():
    parser = argparse.ArgumentParser(description="Selenium")

    # Optional for choose webdriver
    parser.add_argument(
        "-d",
        "--driver",
        default="firefox",
        choices=["firefox", "chrome", "edge"],
        help="webdriver for browser (default: firefox)",
    )

    return parser.parse_args()


def login(browser):
    BASE_URL = "https://login2.scrape.center/"
    USERNAME = "admin"
    PASSWORD = "admin"

    browser.get(BASE_URL)

    form = browser.find_element(By.CLASS_NAME, "el-form")
    form.find_element(By.NAME, "username").send_keys(USERNAME)
    form.find_element(By.NAME, "password").send_keys(PASSWORD)
    form.find_element(
        By.XPATH,
        "//input[@type='submit' and @class='el-button el-button--primary']",
    ).click()


def main():
    args = parse_args()

    if args.driver == "firefox":
        driver = webdriver.Firefox()
    elif args.driver == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("unsupported WebDriver")

    # Open the provided URL
    login(driver)

    input("Pres Enter to close the browser...")
    driver.quit()
