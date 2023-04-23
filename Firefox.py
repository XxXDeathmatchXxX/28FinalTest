import time

from Settings import valid_email, valid_phone, valid_login, driver, url, valid_password, account
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# 1  вход через телефон
def login_phone():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(valid_password)
    print('ВВедите капчу, если необходимо')
    time.sleep(10)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)
    lc = driver.find_element(By.CSS_SELECTOR, 'h3.card-title:nth-child(2)')
    assert lc.text == 'Учетные данные'
    print('Произведен успешный вход в личный кабинет')
    driver.save_screenshot('login_phone.png')
    print('Тест автологин через телефон успешно завершен, скриншот  login_phone.png о проделанной работе сохранен')
    driver.find_element(By.ID, 'logout-btn').click()
    driver.quit()


# 2  вход через email
def login_email():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    login_email = driver.find_element(By.ID, 'username')
    login_email.send_keys(valid_email)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(valid_password)
    password_input.send_keys(Keys.ENTER)
    lc = driver.find_element(By.CSS_SELECTOR, 'h3.card-title:nth-child(2)')
    assert lc.text == 'Учетные данные'
    print('Произведен успешный вход в личный кабинет')
    time.sleep(5)
    driver.save_screenshot('login_email.png')
    print('Тест автологин через email успешно завершен, скриншот  login_email.png о проделанной работе сохранен')
    driver.quit()


# 3 вход через logon(ID)
def login_login():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 't-btn-tab-login').click()
    login_login = driver.find_element(By.ID, 'username')
    login_login.send_keys(valid_login)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(valid_password)
    password_input.send_keys(Keys.ENTER)
    lc = driver.find_element(By.CSS_SELECTOR, 'h3.card-title:nth-child(2)')
    assert lc.text == 'Учетные данные'
    print('Произведен успешный вход в личный кабинет')
    time.sleep(5)
    driver.save_screenshot('login_login.png')
    print('Тест автологин через login успешно завершен, скриншот  login_login.png о проделанной работе сохранен')
    driver.quit()


# 4 вход через лицевой счет
def login_with_self_account():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    login_with_account = driver.find_element(By.ID, 'username')
    login_with_account.send_keys(account)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(valid_password)
    time.sleep(5)
    password_input.send_keys(Keys.ENTER)
    lc = driver.find_element(By.CSS_SELECTOR, 'h3.card-title:nth-child(2)')
    assert lc.text == 'Учетные данные'
    print('Произведен успешный вход в личный кабинет')
    time.sleep(5)
    driver.save_screenshot('login_with_self_account.png')
    print('Тест автологин через account успешно завершен, скриншот  login_with_self_account.png о проделанной работе сохранен')
    driver.quit()










#login_phone()

#login_email()
#login_login()
#login_with_self_account()

