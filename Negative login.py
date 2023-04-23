import time


from Settings import valid_email, valid_phone, valid_login, wrong_password, driver, url
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 5 Неверный вход через телефон
def wrong_login_phone():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(wrong_password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)
    wrong_data = driver.find_element(By.ID, 'form-error-message')
    assert wrong_data.text == 'Неверный логин или пароль'
    print('Неверный логин, либо пароль')
    driver.save_screenshot('wrong_login_phone.png')
    print('Тест автологин через телефон успешно завершен, скриншот  wrong_login_phone.png о проделанной работе сохранен')
    driver.quit()


# 6 Неверный вход через email
def wrong_login_email():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    login_email = driver.find_element(By.ID, 'username')
    login_email.send_keys(valid_email)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(wrong_password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.save_screenshot('wrong_login_email.png')
    print('Тест автологин через email успешно завершен, скриншот  wrong_login_email.png о проделанной работе сохранен')
    #driver.quit()


# 7 Неверный вход через login(ID)
def wrong_login_login():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 't-btn-tab-login').click()
    login_login = driver.find_element(By.ID, 'username')
    login_login.send_keys(valid_login)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(wrong_password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.save_screenshot('wrong_login_login.png')
    print('Тест автологин через login успешно завершен, скриншот  wrong_login_login.png о проделанной работе сохранен')
    driver.quit()


# 8 Неверный вход через лицевой счет
def wrong_login_self_account():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, 'username').send_keys('wrong_account')
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(wrong_password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.save_screenshot('wrong_login_self_account.png')
    print('Тест автологин через login успешно завершен, скриншот  wrong_login_self_account.png о проделанной работе сохранен')
    driver.quit()









#wrong_login_email()
#wrong_login_self_account()
wrong_login_phone()


