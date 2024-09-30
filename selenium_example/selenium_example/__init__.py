import argparse
import json

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
    TIMEOUT = 10

    try:
        load_cookies(browser)
    except FileNotFoundError:
        print("Cookie not found")
        try:
            browser.get(BASE_URL)

            form = WebDriverWait(browser, TIMEOUT).until(
                EC.presence_of_element_located((By.CLASS_NAME, "el-form"))
            )

            form.find_element(By.NAME, "username").send_keys(USERNAME)
            form.find_element(By.NAME, "password").send_keys(PASSWORD)

            # submit_button = WebDriverWait(browser, TIMEOUT).until(
            #     EC.element_to_be_clickable(
            #         (By.CSS_SELECTOR, "button.el-button--primary[type='submit']")
            #     )
            # )
            # submit_button.click()

            # Get current url before login
            initial_url = browser.current_url

            form.find_element(
                By.XPATH,
                "//input[@type='submit' and @class='el-button el-button--primary']",
            ).click()

            WebDriverWait(browser, TIMEOUT).until(EC.url_changes(initial_url))
            print("Login successful")

            print("Store cookies")
            store_cookies(browser)

        except TimeoutException:
            print("Login elements not found or page load timeout.")
        except Exception as e:
            print(f"An error occurred during login: {e}")
    finally:
        try:
            browser.get(BASE_URL)
            WebDriverWait(browser, TIMEOUT).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//button[contains(., 'admin') and contains(@class, 'logout')]",
                    )
                )
            )
        except Exception as e:
            print(f"An error occurred: {e}")


def store_cookies(browser, cookie_path="cookies.json"):
    cookies = browser.get_cookies()
    for cookie in cookies:
        cookie.pop("domain", None)
    with open(cookie_path, "w") as file:
        json.dump(cookies, file)


def load_cookies(browser, cookie_path="cookies.json"):
    with open(cookie_path, "r") as file:
        cookies = json.load(file)
        for cookie in cookies:
            browser.add_cookie(cookie)


def main():
    args = parse_args()

    if args.driver == "firefox":
        driver = webdriver.Firefox()
    elif args.driver == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("unsupported WebDriver")

    login(driver)

    input("Pres Enter to close the browser...")
    driver.quit()
