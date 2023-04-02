
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locator

class TestRegistration:

	def test_registration(self, driver): # объявляем функцию регистрации (первое слово в тестах всегда test) и в качестве аргумента передаём ей фикстуру driver
		driver.find_element(*Locator.CLICK_ON_LOGIN).click()                      # клик по кнопке "Войти в аккаунт"
		driver.find_element(*Locator.CLICK_ON_TEXT_SIGN_UP).click()               # клик по надписи Зарегистрироваться в форме авторизации
		driver.find_element(*Locator.ENTER_NAME).send_keys(Locator.VALID_NAME)      # ввести имя
		driver.find_element(*Locator.ENTER_EMAIL_2).send_keys(Locator.VALID_EMAIL)  # ввести Email
		driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Locator.VALID_PASSWORD)  # ввести пароль
		driver.find_element(*Locator.CLICK_ON_BUTTON_SIGN_UP).click()               # клик по кнопке Зарегистрироваться
		user_reg = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.USER_ON))).text
		assert user_reg == "Такой пользователь уже существует"



	def test_error_reg(self,driver):                                               # проверка на ошибку при вводе невалидного пароля.
		driver.find_element(*Locator.CLICK_ON_LOGIN).click()                       # клик по кнопке "Войти в аккаунт"
		driver.find_element(*Locator.CLICK_ON_TEXT_SIGN_UP).click()                # клик по надписи Зарегистрироваться)
		driver.find_element(*Locator.ENTER_NAME).send_keys(Locator.VALID_NAME)     # ввести имя
		driver.find_element(*Locator.ENTER_EMAIL_2).send_keys(Locator.VALID_EMAIL)   # ввести Email
		driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Locator.INVALID_PASSWORD)  # ввести не валидный пароль
		driver.find_element(*Locator.CLICK_ON_BUTTON_SIGN_UP).click()              # клик по кнопке Зарегистрироваться
		pass_reg_error = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.WAIT_ERROR))).text  # ожидание появления ошибки
		assert pass_reg_error == 'Некорректный пароль'

