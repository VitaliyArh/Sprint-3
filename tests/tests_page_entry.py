from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locator import Locator

class TestEntry:

	def test_entry_button_log_into_account(self, driver):
		driver.find_element(*Locator.CLICK_ON_LOGIN).click()
		driver.find_element(*Locator.ENTER_EMAIL_1).send_keys(Data.VALID_EMAIL)
		driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Data.VALID_PASSWORD)
		driver.find_element(*Locator.CLICK_BUTTON_TO_COME_IN).click()
		text_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locator.WAIT_BUTTON_CHECKOUT))).text
		assert text_button == 'Оформить заказ'

	def test_login_Personal_account(self, driver):
		driver.find_element(*Locator.CLICK_PERSONAL_AREA_HOME_PAGE).click()
		driver.find_element(*Locator.ENTER_EMAIL_1).send_keys(Data.VALID_EMAIL)
		driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Data.VALID_PASSWORD)
		driver.find_element(*Locator.CLICK_BUTTON_TO_COME_IN).click()
		text_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locator.WAIT_BUTTON_CHECKOUT))).text
		assert text_button == 'Оформить заказ'

	def test_login_via_registration_form_button(self, driver):
		driver.find_element(*Locator.CLICK_ON_LOGIN).click()
		driver.find_element(*Locator.CLICK_ON_TEXT_SIGN_UP).click()
		driver.find_element(*Locator.CLICK_ON_TEXT_LOGIN_1).click()
		driver.find_element(*Locator.ENTER_EMAIL_1).send_keys(Data.VALID_EMAIL)
		driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Data.VALID_PASSWORD)
		driver.find_element(*Locator.CLICK_BUTTON_TO_COME_IN).click()
		text_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locator.WAIT_BUTTON_CHECKOUT))).text
		assert text_button == 'Оформить заказ'

	def test_login_via_password_recovery_form_button(self, driver):
		driver.find_element(*Locator.CLICK_ON_LOGIN).click()
		driver.find_element(*Locator.CLICK_ON_TEXT_RECOVER_PASSWORD).click()
		driver.find_element(*Locator.CLICK_ON_TEXT_LOGIN_2).click()
		driver.find_element(*Locator.ENTER_EMAIL_1).send_keys(Data.VALID_EMAIL)
		driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Data.VALID_PASSWORD)
		driver.find_element(*Locator.CLICK_BUTTON_TO_COME_IN).click()
		text_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locator.WAIT_BUTTON_CHECKOUT))).text
		assert text_button == 'Оформить заказ'
