from selenium import webdriver

valid_email = 'dr.kireal@yandex.ru'
valid_password = 'Kireal36'
valid_phone = '+79263103151'
valid_login = 'rtkid_1681561996811'
wrong_password = 'Kireal36!'
account = 'SomeAccountNumber'
url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=83fb1368-3599-412e-a82b-a8b1f0afa835&theme&auth_type#/'
vk_password = 'YourCorrectPassword'
driver = webdriver.Firefox()

name = 'Вася'
second_name = 'Пупкин'
register_email = 'Vasya@yandex.ru'
password = 'Vasya35!'