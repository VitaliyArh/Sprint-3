from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locator

class TestPersonalAccount:
	def test_go_to_personal_account(self, go_to_personal_account):
		driver = go_to_personal_account
		driver.find_element(*Locator.CLICK_PERSONAL_AREA_HOME_PAGE).click()
		personal_profile = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.WAIT_LABEL_PROFILE))).text
		assert personal_profile == 'Профиль'
