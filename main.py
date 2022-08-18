from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import re
import time
from webdriver_manager.chrome import ChromeDriverManager


def main():
    username = "watarfak@gmail.com"
    password = "rankmybrain123"
    url = "https://rankyourbrain.com/mental-math/mental-math-test-easy/play"
    login_url = "https://rankyourbrain.com/"
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(login_url)
    input("Press Enter to continue...")
    driver.get(url)
    while True:
        beforeAnswerElement = driver.find_elements(By.ID, "beforeAnswer")
        answerElement = driver.find_elements(By.ID, "answer")
        if not beforeAnswerElement and not answerElement:
            break
        beforeAnswer, answerElement = beforeAnswerElement[0], answerElement[0]
        match = re.match('(?P<firstNum>\d+) (?P<operation>.) (?P<secondNum>\d+)', beforeAnswer.text).groupdict()
        answer = compute(int(match["firstNum"]), int(match["secondNum"]), match["operation"])
        answerElement.send_keys(answer)
        time.sleep(0.59)
    input("Press Enter to continue...")


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

def get_sleep_time(targetResult):
    return targetResult / 120

if __name__ == "__main__":
    main()
