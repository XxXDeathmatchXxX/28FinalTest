import time

from Settings import driver, url, name, second_name, register_email, password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 17 Автотест на регистрацию
def register():
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.CSS_SELECTOR, '.name-container > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)').send_keys(name)
    driver.find_element(By.CSS_SELECTOR, '.name-container > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)').send_keys(second_name)
    driver.find_element(By.CSS_SELECTOR, '#address').send_keys(register_email)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'password-confirm').send_keys(password)
    window_first = driver.window_handles[0]
    driver.find_element(By.CSS_SELECTOR, '.rt-link').click()
    time.sleep(3)
    driver.switch_to.window(window_first)
    driver.find_element(By.CSS_SELECTOR, '.rt-btn').click()
    registration_text = driver.find_element(By.CSS_SELECTOR, '.card-container__title')
    assert registration_text.text == 'Подтверждение email'
    print("Регистрация успешно проведена")
    driver.quit()

register()