# тесты страницы Выход из аккаунта

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions # as EC

from locator import Locator


class TestLogout:

	def test_logout_of_system_clicking_logout_button_your_account(self, go_to_personal_account):
		driver = go_to_personal_account
		driver.find_element(*Locator.CLICK_PERSONAL_AREA_HOME_PAGE).click()    # Клик по кнопке "Личный кабинет на главной странице"
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locator.WAIT_LABEL_PROFILE_OK)))  # Явное ожидание загрузки формы личного кабинета
		driver.find_element(*Locator.CLICK_BUTTON_EXIT).click()                 # клик по кнопке "Выход" в личном кабинете
		exit_logout = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locator.WAIT_LOGIN_PAGE))).text
		assert exit_logout == "Вход"


