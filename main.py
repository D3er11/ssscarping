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


print("Okay, Let's go!!")

TOKEN = "6081536762:AAEooblcrUTv0SENSRdFtaW32IyqMxLVeaQ"
chat_id = "785316401"
message = "test Found ticket"
page = 'https://pass.rw.by/ru/route/?from=%D0%9C%D0%BE%D0%B3%D0%B8%D0%BB%D1%91%D0%B2&from_exp=2100150&from_esr=156609&to=%D0%9C%D0%B8%D0%BD%D1%81%D0%BA&to_exp=2100000&to_esr=140210&date=today&type=1#'
pythonResponse = requests.get(page)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

options = webdriver.ChromeOptions()
options.add_argument("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
#options.add_argument("--headless")
s = Service(executable_path="/home/realangrymedvedegb/egbscrap/chromedriver")
driver = webdriver.Chrome(
    service=s,
    options=options
)
driver.maximize_window()
driver.get("https://egbet.live/play/simple_bets#auth")
time.sleep(3)
username = driver.find_element(By.ID, "field-log-login")
password = driver.find_element(By.ID, "field-log-password")
username.send_keys("realangrymedved")
time.sleep(2)
password.send_keys("Alexegb8")
time_before_solve = datetime.now()
solver = TwoCaptcha('6b110d874e22f0023b1a12484002fbe2')
result = solver.recaptcha(
    sitekey="6LdcP4oUAAAAAG88ESQr1NucEYZbVl5-jxQZtw78",
    url="https://egbet.live/play/simple_bets#auth"
)
code = result['code']
balance = solver.balance()
print(balance)
print(code)
time_after_solve = datetime.now()
solve_time = time_after_solve - time_before_solve
print("Solve time: ", round(solve_time.total_seconds()))
driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "button-adaptive").click()
time.sleep(3)
driver.get("https://egbet.live/")
time.sleep(5)
site_balance = driver.find_element(By.CLASS_NAME, "user__balance--value").text
print(site_balance)
try:
    driver.find_element(By.XPATH, "//*[@class='cookies-panel__close js-close-block-btn']").click()
except Exception as e:
    print(e)
try:
    driver.find_element(By.XPATH, "//*[@class='cookies-panel__close js-close-block-btn']").click()
except Exception as e:
    print(e)
time.sleep(5)
for i in range(1, 4500):
    print('Giveaway number: ', i)
    fail_attempts = 0
    success_attempts = 0
    while fail_attempts < 5 and success_attempts < 1:
        driver.get("https://egbet.live/")
        print('reloaded page now need to sleep')
        sleep_time_random = random.randint(9, 15)
        time.sleep(sleep_time_random)
        #driver.find_element("body").send_keys(Keys.CONTROL + Keys.HOME)
        print('trying to participate in giveaway')
        prize_description = driver.find_element(By.CLASS_NAME, "giveaway-prize__description").text
        bonus_word = 'Бонус'
        if bonus_word in prize_description:
            print('pass shit ' + prize_description)
            time_now = datetime.today().strftime('%H:%M:%S %p')
            loot_time = datetime.today() + timedelta(seconds=1670)
            loot_time = loot_time.strftime('%H:%M %p')
            print("Need to sleep after bonus: ", time_now)
            print("Awake time after bonus: ", loot_time)
            sleep_time_random = random.randint(1778, 1798)
            time.sleep(sleep_time_random)
            print("work work")
            continue
        else:
            print("LEEET'S GOOOOO " + prize_description)

        try:
            driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[4]/div/aside/div/div[5]/div[2]/div[1]/button").click()
            success_attempts += 1
            print(f"iam participator and have: {success_attempts} success_attempts, with only {fail_attempts} fail attempts")
        except Exception as e:
            print(e)
            fail_attempts += 1
            if fail_attempts > 0:
                try:
                    driver.find_element(By.XPATH, '//button[text()="Take a part"]')
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





'''
python.exe -m pip install --upgrade pip
pip install selenium
pip3 install 2captcha-python

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
