import time

from Settings import  valid_phone, driver, url, valid_password, vk_password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 18 переход на сайт ростелекома
def rostelecom_site():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(valid_password)
    password_input.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'rt-btn').click()
    url_main = 'https://msk.rt.ru/'
    assert (url_main)
    print('успешно произведен переход на основной сайт Ростелекома')
    driver.quit()



# 19 Соц сети
def Socials():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(valid_password)
    password_input.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'socials_action').click()
    driver.find_element(By.CSS_SELECTOR, 'svg.social-icon:nth-child(2)').click()
    social_check = driver.find_element(By.CSS_SELECTOR, '.ext-widget_h_tx')
    assert social_check.text == 'Одноклассники'
    print('Успешно произведен переход по кнопке для привязки соц сетей')
    driver.quit()


# 20 выход из личного кабинета
def Quit():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(valid_password)
    password_input.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'logout-btn').click()
    authorization = driver.find_element(By.CSS_SELECTOR, '.card-container__title')
    assert authorization.text == 'Авторизация'
    print('Успешнов прошел вход и выход из личного кабинета')
    driver.quit()


# 21 Предусловие соц сеть привязана, заходим через соц сеть
def Enter_with_social_vk():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '#oidc_vk > svg:nth-child(1)').click()
    login = driver.find_element(By.CSS_SELECTOR, '.box_msg_gray')
    assert login.text == 'Для продолжения вам необходимо войти ВКонтакте.'
    driver.find_element(By.CSS_SELECTOR, 'input.oauth_form_input:nth-child(7)').send_keys(valid_phone)
    driver.find_element(By.CSS_SELECTOR, 'input.oauth_form_input:nth-child(9)').send_keys(vk_password)
    driver.find_element(By.ID, 'install_allow').click()
    lc = driver.find_element(By.CSS_SELECTOR, 'h3.card-title:nth-child(2)')
    assert lc.text == 'Учетные данные'
    print('Авторизация через соц сеть Вконтакте успешно работает')
    driver.quit()


# 22 Кнопка одноклассники
def Enter_with_social_ok():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '#oidc_ok > svg:nth-child(1)').click()
    login = driver.find_element(By.CSS_SELECTOR, '.ext-widget_h_tx')
    assert login.text == 'Одноклассники'
    print('Кнопка входа через Одноклассники успешно работает')
    driver.quit()

# 23 Yandex
def Enter_with_social_yandex():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '#oidc_ya > svg:nth-child(1)').click()
    login = driver.find_element(By.CSS_SELECTOR, '.passp-add-account-page-title')
    assert login.text == 'Войдите с Яндекс ID'
    print('Кнопка входа через Yandex успешно работает')
    driver.quit()


# 24 Google
def Enter_with_social_google():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'oidc_google').click()
    login = driver.find_element(By.CSS_SELECTOR, '.kHn9Lb')
    assert login.text == 'Войдите в аккаунт Google'
    print('Кнопка входа через Google успешно работает')
    driver.quit()


# 25 Мой мир
def Enter_with_social_moimir():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'oidc_mail').click()
    login = driver.find_element(By.CSS_SELECTOR, '.content > h1:nth-child(1)')
    assert login.text == 'Необходим доступ к вашим данным'
    print('Кнопка входа через Мой Мир успешно работает')
    driver.quit()



#rostelecom_site()
#Socials()
#Quit()
#Enter_with_social_vk()
#Enter_with_social_ok()
#Enter_with_social_yandex()
#Enter_with_social_google()
Enter_with_social_moimir()