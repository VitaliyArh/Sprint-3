# тесты страницы вход(авторизация)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locator import Locator


class TestEntry:
	def test_entry_button_log_into_account(self, log_into_account): # вход по кнопке «Войти в аккаунт» на главной странице
		driver = log_into_account
		driver.find_element(*Locator.CLICK_BUTTON_TO_COME_IN).click()  # клик по кнопке Войти в форме авторизации
		text_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locator.WAIT_BUTTON_CHECKOUT))).text
		assert text_button == 'Оформить заказ'



	def test_login_Personal_account(self, login_through_Personal_account):     # вход по кнопке «Личный кабинет»
		driver = login_through_Personal_account
		driver.find_element(*Locator.CLICK_BUTTON_TO_COME_IN).click()   # клик по кнопке Войти в форме авторизации
		text_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locator.WAIT_BUTTON_CHECKOUT))).text
		assert text_button == 'Оформить заказ'



	def test_login_via_registration_form_button(self, login_via_registration_form_button): # вход через надпись "Войти" в форме регистрации
		driver = login_via_registration_form_button
		driver.find_element(*Locator.CLICK_BUTTON_TO_COME_IN).click()        # клик по кнопке Войти в форме авторизации
		text_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locator.WAIT_BUTTON_CHECKOUT))).text
		assert text_button == 'Оформить заказ'



	def test_login_via_password_recovery_form_button(self, login_via_password_recovery_form_button): # вход через кнопку в форме восстановления пароля.
		driver = login_via_password_recovery_form_button
		driver.find_element(*Locator.CLICK_BUTTON_TO_COME_IN).click()  # клик по кнопке Войти в форме авторизации
		text_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locator.WAIT_BUTTON_CHECKOUT))).text
		assert text_button == 'Оформить заказ'


