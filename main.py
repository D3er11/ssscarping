from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from twocaptcha import TwoCaptcha
from datetime import datetime, timedelta
import time
import random
import requests

TOKEN = "6081536762:AAEooblcrUTv0SENSRdFtaW32IyqMxLVeaQ"
chat_id = "785316401"
message = "test Found ticket"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
egb_user = "realangrymedved"
egb_pass = "Alexegb8"
solver = TwoCaptcha('6b110d874e22f0023b1a12484002fbe2')
driver = webdriver.Chrome()


def egb_auth():
    driver.maximize_window()
    driver.get("https://egamingbet.net/play/simple_bets#auth")
    time.sleep(3)
    username = driver.find_element(By.ID, "field-log-login")
    password = driver.find_element(By.ID, "field-log-password")
    username.send_keys(egb_user)
    time.sleep(2)
    password.send_keys(egb_pass)
    time_before_solve = datetime.now()
    result = solver.recaptcha(
        sitekey="6LdcP4oUAAAAAG88ESQr1NucEYZbVl5-jxQZtw78",
        url="https://egamingbet.net/play/simple_bets#auth"
    )
    code = result['code']
    balance = solver.balance()
    print(balance)
    print(code)
    time_after_solve = datetime.now()
    solve_time = time_after_solve - time_before_solve
    print("Solve time: ", round(solve_time.total_seconds()))

    driver.execute_script(
        "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")

    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "button-adaptive").click()


def garbage_removing():
    time.sleep(3)
    driver.get("https://egamingbet.net/")
    time.sleep(5)
    try:
        driver.find_element(By.XPATH, "//*[@class='cookies-panel__close js-close-block-btn']").click()
    except Exception as e:
        print(e)
    try:
        driver.find_element(By.XPATH, "//*[@class='btn btn--gray-invert js-close-block-btn']").click()
    except Exception as e:
        print(e)


def giveaway_participator():
    time.sleep(5)
    for i in range(1, 4500):
        print('Giveaway number: ', i)
        fail_attempts = 0
        success_attempts = 0
        while fail_attempts < 5 and success_attempts < 1:
            driver.get("https://egamingbet.net/")
            print('Prepare for participation')
            sleep_time_random = random.randint(9, 15)
            time.sleep(sleep_time_random)
            print('Trying to participate in giveaway')
            bonus = driver.find_element(By.CLASS_NAME, "giveaway-prize__description").text
            bonus_word = 'Бонус'
            bonus_word2 = 'Bonus'
            if bonus_word in bonus or bonus_word2 in bonus:
                print('pass shit ' + bonus)
                time_now = datetime.today().strftime('%H:%M:%S %p')
                loot_time = datetime.today() + timedelta(seconds=1670)
                loot_time = loot_time.strftime('%H:%M %p')
                print("Need to sleep after bonus: ", time_now)
                print("Awake time after bonus: ", loot_time)
                sleep_time_random = random.randint(1650, 1670)
                time.sleep(sleep_time_random)
                print("work work")
                continue
                # в какой итерации начинает continue в while или в for?
            else:
                print("LEEET'S GOOOOO " + bonus)

            try:
                driver.find_element(By.XPATH,
                                    "/html/body/div[2]/div[1]/div[4]/div/aside/div/div[4]/div[2]/div[1]/button").click()
                success_attempts += 1
                print(
                    f"iam participator and have: {success_attempts} success_attempts, with only {fail_attempts} fail attempts")
            except Exception as e:
                print(e)
                fail_attempts += 1
                try:
                    driver.find_element(By.XPATH, '//button[text()="Take a part"]')
                    # Добавить тут Take a part or Принять участие
                    success_attempts += 1
                except Exception as e:
                    fail_attempts += 1
                    print(e)

        if fail_attempts == 5:
            print(requests.get(url).json())
        time_now = datetime.today().strftime('%H:%M:%S %p')
        loot_time = datetime.today() + timedelta(seconds=1670)
        loot_time = loot_time.strftime('%H:%M %p')
        print("Need to sleep: ", time_now)
        print("Awake time: ", loot_time)
        sleep_time_random = random.randint(1650, 1670)
        time.sleep(sleep_time_random)
        print("work work")


if __name__ == "__main__":
    print("Okay, Let's go!!")
    egb_auth()
    garbage_removing()
    giveaway_participator()

'''
python.exe -m pip install --upgrade pip
pip install selenium
pip3 install 2captcha-python


Придумать как ставить в рандом время,
сделать переменную в начале, в которой будет время предыдущего участия
или парсить время конкурса и участвовать в зависимости от него рандомно.
В начале проверку, is giveaway button is active.
Check every 10 min, until it will be active.
Если кнопка активна и появляется уведомление, о том,
что нет ставок, найти игру, которая будет через 1 день,
сделать ставку 1$, перейти в мои ставки и отменить ее.
Добавить парсинг последние победители,
если там имя realangrymedved
тогда отправить уведомление в телеграм
и остановить цикл.
Оформить все это в класс,
запустить с командной строки,
опробовать click library.
Хаходить на главную страницу, а не на страницу с авторизацией.
Посчитать, сколько времени я трачу на авторизацию, уменьшить sleep.
Настроить выдачу всех ошибок в try, отправлять ошибки в телеграм.
Придумать проверку на приз в виде скинов,
Узнать, как происходит передача.
Настроить прием.
'''
