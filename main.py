from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import re
import time
from webdriver_manager.chrome import ChromeDriverManager


def main():
    url = "https://rankyourbrain.com/mental-math/mental-math-test-easy/play"
    login_url = "https://rankyourbrain.com/"
    sleep_time = get_sleep_time()
    driver = setup(url, login_url)

    while True:
        before_answer_element = driver.find_elements(By.ID, "beforeAnswer")
        answer_element = driver.find_elements(By.ID, "answer")
        if not before_answer_element and not answer_element:
            break
        beforeAnswer, answer_element = before_answer_element[0], answer_element[0]
        match = re.match('(?P<firstNum>\d+) (?P<operation>.) (?P<secondNum>\d+)', beforeAnswer.text).groupdict()
        answer = compute(int(match["firstNum"]), int(match["secondNum"]), match["operation"])
        answer_element.clear()
        answer_element.send_keys(answer)
        time.sleep(sleep_time)
    print("Script finished! You may close your browser window when you're done taking a look at your new highscore.")


def compute(firstNumber, secondNumber, operation):
    result = 0
    if operation == '*':
        result = firstNumber * secondNumber
    elif operation == '/':
        result = firstNumber / secondNumber
    elif operation == '+':
        result = firstNumber + secondNumber
    elif operation == '-':
        result = firstNumber - secondNumber

    return int(result)


def get_sleep_time():
    target_result = int(input("Please tell me, what is the score you would like to achieve?"))
    if target_result > 200:
        target_result = 200
    return 120 / (target_result + 10)


def setup(url, login_url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(login_url)
    input("You will be asked to enter login details. Once you do this, press any key in this terminal. "
          "If you don't want to login (to save your score), just press any key now.")
    driver.get(url)
    return driver


if __name__ == "__main__":
    main()
