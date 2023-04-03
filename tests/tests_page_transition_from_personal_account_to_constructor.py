from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locator import Locator

class TestJumpConstructor:

	def test_from_your_personal_account_click_constructor(self, go_to_personal_account):
		driver = go_to_personal_account
		driver.find_element(*Locator.CLICK_PERSONAL_AREA_HOME_PAGE).click()
		WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/account/profile' and text()='Профиль']")))
		driver.find_element(*Locator.CLICK_BUTTON_CONSTRUCTOR_PERSONAL_OFFICE).click()
		personal_account_constructor = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.WAIT_PAGE_CONSTRUCTOR))).text
		assert personal_account_constructor == 'Соберите бургер'

	def test_from_your_personal_account_click_logo_stellarburger(self, go_to_personal_account):
		driver = go_to_personal_account
		driver.find_element(*Locator.CLICK_PERSONAL_AREA_HOME_PAGE).click()
		WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.WAIT_LABEL_PROFILE)))
		driver.find_element(*Locator.CLICK_LOGO_STELLAR_BURGER).click()                                 
		personal_account_constructor = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.WAIT_PAGE_CONSTRUCTOR))).text
		assert personal_account_constructor == 'Соберите бургер'
