import time


from Settings import valid_email, valid_phone,valid_login, account, driver, url
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 9 автотест на воостановление пароля по телефону через email
def forgot_password_phone_email():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    time.sleep(10)
    driver.find_element(By.ID, 'reset').click()
    driver.find_element(By.CSS_SELECTOR, 'label.rt-radio:nth-child(2) > span:nth-child(2) > span:nth-child(3) > span:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'button.rt-btn:nth-child(2)').click()
    reset_password = driver.find_element(By.CSS_SELECTOR, '.card-container__title')
    assert reset_password.text == 'Восстановление пароля'
    print('Сброс пароля по номеру телефона через email успешно прошел')
    driver.quit()


# 10 автотест на воостановление пароля по телефону через смс
def forgot_password_phone():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    time.sleep(10)
    driver.find_element(By.ID, 'reset').click()
    driver.find_element(By.CSS_SELECTOR, 'label.rt-radio:nth-child(1) > span:nth-child(2) > span:nth-child(3) > span:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'button.rt-btn:nth-child(2)').click()
    reset_password = driver.find_element(By.CSS_SELECTOR, '.card-container__title')
    if(reset_password):
        assert reset_password.text == 'Восстановление пароля'
        print('Сброс пароля по номеру телефона через смс успешно прошел')
    else:
        print('wrong')

    driver.quit()


# 11 автотест на воостановление пароля по email через email
def forgot_password_email():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    time.sleep(10)
    print('Введите капчу')
    driver.find_element(By.ID, 'reset').click()
    driver.find_element(By.CSS_SELECTOR, 'label.rt-radio:nth-child(2) > span:nth-child(2) > span:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'button.rt-btn:nth-child(2)').click()
    reset_password = driver.find_element(By.CSS_SELECTOR, '.card-container__title')
    if (reset_password):
        assert reset_password.text == 'Восстановление пароля'
        print('Сброс пароля по номеру телефона через смс успешно прошел')
    else:
        print('wrong')

    driver.quit()


# 12 автотест на воостановление пароля на email через sms
def forgot_password_email_phone():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    time.sleep(10)
    print('Введите капчу')
    driver.find_element(By.ID, 'reset').click()
    driver.find_element(By.CSS_SELECTOR, 'label.rt-radio:nth-child(1) > span:nth-child(2) > span:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'button.rt-btn:nth-child(2)').click()
    reset_password = driver.find_element(By.CSS_SELECTOR, '.card-container__title')
    if (reset_password):
        assert reset_password.text == 'Восстановление пароля'
        print('Сброс пароля по номеру телефона через смс успешно прошел')
    else:
        print('wrong')

    driver.quit()


# 13 автотест на воостановление пароля на вход через логин(ID) по смс
def forgot_login_phone():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    print('Введите капчу при необходимости')
    time.sleep(10)
    driver.find_element(By.ID, 'reset').click()
    driver.find_element(By.CSS_SELECTOR, 'label.rt-radio:nth-child(1) > span:nth-child(2) > span:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'button.rt-btn:nth-child(2)').click()
    reset_password = driver.find_element(By.CSS_SELECTOR, '.card-container__title')
    if (reset_password):
        assert reset_password.text == 'Восстановление пароля'
        print('Сброс пароля по логину через смс успешно прошел')
    else:
        print('wrong')

    driver.quit()


# 14 автотест на воостановление пароля на вход через логин(ID) по email
def forgot_login_phone_email():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    print('Введите капчу при необходимости')
    time.sleep(10)
    driver.find_element(By.ID, 'reset').click()
    driver.find_element(By.CSS_SELECTOR, 'label.rt-radio:nth-child(2) > span:nth-child(2) > span:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'button.rt-btn:nth-child(2)').click()
    reset_password = driver.find_element(By.CSS_SELECTOR, '.card-container__title')
    if (reset_password):
        assert reset_password.text == 'Восстановление пароля'
        print('Сброс пароля по логину через email успешно прошел')
    else:
        print('wrong')

    driver.quit()


# 15 автотест на воостановление пароля на вход через лицевой счет  по sms
def forgot_login_login_phone():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, 'username').send_keys(account)
    print('Введите капчу при необходимости')
    time.sleep(10)
    driver.find_element(By.ID, 'reset').click()
    driver.find_element(By.CSS_SELECTOR, 'label.rt-radio:nth-child(1) > span:nth-child(2) > span:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'button.rt-btn:nth-child(2)').click()
    reset_password = driver.find_element(By.CSS_SELECTOR, '.card-container__title')
    if (reset_password):
        assert reset_password.text == 'Восстановление пароля'
        print('Сброс пароля по лицевому счету через телефон успешно прошел')
    else:
        print('wrong')

    driver.quit()


# 16 автотест на воостановление пароля на вход через лицевой счет по email
def forgot_login_login_email():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, 'username').send_keys(account)
    print('Введите капчу при необходимости')
    time.sleep(10)
    driver.find_element(By.ID, 'reset').click()
    driver.find_element(By.CSS_SELECTOR, 'label.rt-radio:nth-child(2) > span:nth-child(2) > span:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'button.rt-btn:nth-child(2)').click()
    reset_password = driver.find_element(By.CSS_SELECTOR, '.card-container__title')
    if (reset_password):
        assert reset_password.text == 'Восстановление пароля'
        print('Сброс пароля по лицевому счету через email успешно прошел')
    else:
        print('wrong')

    driver.quit()



#forgot_password_phone_email()
#forgot_password_phone()
#forgot_password_email()
#forgot_password_email_phone()
#forgot_login_phone()
#forgot_login_phone_email()
#forgot_login_login_phone()
#forgot_login_login_email()