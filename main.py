## TODO добавить рекапчу


import random
from time import sleep
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mails_array = []
with open("mails.txt") as file:
    mails_array = [row.strip() for row in file]

proxy_array = []
with open("proxy.txt") as file:
    proxy_array = [row.strip() for row in file]


def get_random_proxy():
    proxy_str = random.choice(proxy_array)
    proxy_options = {"proxy": {"https": f"https://{proxy_str}"}}
    return proxy_options


for _ in range(len(mails_array)):

    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en-US")

    browser = webdriver.Chrome(
        ChromeDriverManager().install(), seleniumwire_options=get_random_proxy()
    )

    browser.get("https://kawsone.com/password")

    sleep(1)

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//a[text()="MAILING LIST"]'))
    ).click()

    sleep(2)

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@type="email"]'))
    ).send_keys(mails_array[_])

    sleep(2)

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]'))
    ).click()

    print(f"Почта {mails_array[_]} отправлена")

    sleep(2)
