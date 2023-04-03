from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locator
from data import Data

class TestRegistration:

	def test_registration(self, driver):
		driver.find_element(*Locator.CLICK_ON_LOGIN).click()
		driver.find_element(*Locator.CLICK_ON_TEXT_SIGN_UP).click()
		driver.find_element(*Locator.ENTER_NAME).send_keys(Data.VALID_NAME)
		driver.find_element(*Locator.ENTER_EMAIL_2).send_keys(Data.VALID_EMAIL)
		driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Data.VALID_PASSWORD)
		driver.find_element(*Locator.CLICK_ON_BUTTON_SIGN_UP).click()
		user_reg = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.USER_ON))).text
		assert user_reg == Data.TEXT_ERROR_1

	def test_error_reg(self,driver):
		driver.find_element(*Locator.CLICK_ON_LOGIN).click()
		driver.find_element(*Locator.CLICK_ON_TEXT_SIGN_UP).click()
		driver.find_element(*Locator.ENTER_NAME).send_keys(Data.VALID_NAME)
		driver.find_element(*Locator.ENTER_EMAIL_2).send_keys(Data.VALID_EMAIL)
		driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Data.INVALID_PASSWORD)
		driver.find_element(*Locator.CLICK_ON_BUTTON_SIGN_UP).click()
		pass_reg_error = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.WAIT_ERROR))).text
		assert pass_reg_error == Data.TEXT_ERROR_2
