
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from locator import Locator


url = 'https://stellarburgers.nomoreparties.site/'
                                                     # фикстура перехода на сайт и регистрации
@pytest.fixture(scope='function') # чтобы экземпляр браузера запускался по новой для каждого теста, потому что тесты должны быть изолированными
def driver():                                        # объявляем функцию driver потому что будем делать webdriver
    options = Options()                              # Импортировали Options из selenium.webdriver.chrome.options
    options.add_argument("--window-size=1200,600")   # аргумент опции размера окна браузера
    browser = webdriver.Chrome(options=options)      # будем консолидировать наш браузер и передаём в него опции
    browser.get(url)                                 # чтобы откррыть ресурс пишем browser.get и указываем url

    yield browser
    browser.quit()




@pytest.fixture(scope='function')     # вход по кнопке «Войти в аккаунт» на главной странице
def log_into_account(driver):         # передаём в эту фикстуру , первую, предыдущую фикстуру, в виде аргумента driver - чтобы не писать один и тот же код
    driver.find_element(*Locator.CLICK_ON_LOGIN).click()                              # клик по кнопке "Войти в аккаунт"
    driver.find_element(*Locator.ENTER_EMAIL_1).send_keys(Locator.VALID_EMAIL)        # ввести Email
    driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Locator.VALID_PASSWORD)    # ввести пароль
    return driver



@pytest.fixture(scope = 'function')
def login_through_Personal_account(driver):                                  # вход по кнопке «Личный кабинет»
    driver.find_element(*Locator.CLICK_PERSONAL_AREA_HOME_PAGE).click()   # Клик по кнопке "Личный кабинет"
    driver.find_element(*Locator.ENTER_EMAIL_1).send_keys(Locator.VALID_EMAIL)  # ввести Email
    driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Locator.VALID_PASSWORD)  # ввести пароль
    return driver



@pytest.fixture(scope = 'function')
def login_via_registration_form_button(driver):                                 # вход через кнопку в форме регистрации
    driver.find_element(*Locator.CLICK_ON_LOGIN).click()          # клик по кнопке "Войти в аккаунт"
    driver.find_element(*Locator.CLICK_ON_TEXT_SIGN_UP).click()  # клик по надписи Зарегистрироваться) в форме авторизации
    driver.find_element(*Locator.CLICK_ON_TEXT_LOGIN_1).click()                    # клик по надписи "Войти" в форме регистации
    driver.find_element(*Locator.ENTER_EMAIL_1).send_keys(Locator.VALID_EMAIL)  # ввести Email
    driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Locator.VALID_PASSWORD)  # ввести пароль
    return driver



@pytest.fixture(scope = 'function')
def login_via_password_recovery_form_button(driver): # вход через кнопку в форме восстановления пароля
    driver.find_element(*Locator.CLICK_ON_LOGIN).click()  # клик по кнопке "Войти в аккаунт"
    driver.find_element(*Locator.CLICK_ON_TEXT_RECOVER_PASSWORD).click() # клик по надписи "Восстановить пароль"
    driver.find_element(*Locator.CLICK_ON_TEXT_LOGIN_2).click()  # клик по надписи "Войти" в форме восстановление пароля
    driver.find_element(*Locator.ENTER_EMAIL_1).send_keys(Locator.VALID_EMAIL)  # ввести Email
    driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Locator.VALID_PASSWORD)  # ввести пароль
    return driver



@pytest.fixture(scope = 'function') # Вход в личный кабинет. # Переход в конструктор.
def go_to_personal_account(driver):
    driver.find_element(*Locator.CLICK_PERSONAL_AREA_HOME_PAGE).click()  # Клик по кнопке "Личный кабинет"
    driver.find_element(*Locator.ENTER_EMAIL_1).send_keys(Locator.VALID_EMAIL)  # ввести Email
    driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Locator.VALID_PASSWORD)  # ввести пароль
    driver.find_element(*Locator.CLICK_BUTTON_TO_COME_IN).click()  # клик по кнопке Войти в форме авторизации
    return driver











