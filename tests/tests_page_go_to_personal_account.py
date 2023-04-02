# тесты страницы переход в личный кабинет

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locator


class TestPersonalAccount:
	def test_go_to_personal_account(self, go_to_personal_account):             # Переход в профиль по клику кнопки «Личный кабинет»
		driver = go_to_personal_account
		driver.find_element(*Locator.CLICK_PERSONAL_AREA_HOME_PAGE).click()     # Клик по кнопке "Личный кабинет на главной странице"
		personal_profile = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.WAIT_LABEL_PROFILE))).text
		assert personal_profile == 'Профиль'

