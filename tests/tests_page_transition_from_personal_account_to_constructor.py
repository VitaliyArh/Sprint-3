# тесты страницы переход из личного кабинета в конструктор

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locator import Locator


class TestJumpConstructor:

	def test_from_your_personal_account_click_constructor(self, go_to_personal_account):   # Переход из профиля личного кабинета в конструктор по клику кнопке "Конструктор"
		driver = go_to_personal_account
		driver.find_element(*Locator.CLICK_PERSONAL_AREA_HOME_PAGE).click()   # Клик по кнопке "Личный кабинет на главной странице"
		WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/account/profile' and text()='Профиль']"))) # Явное ожидание загрузки формы личного кабинета
		driver.find_element(*Locator.CLICK_BUTTON_CONSTRUCTOR_PERSONAL_OFFICE).click() # клик по кнопке "Конструктор" в личном кабинете и переход в форму "Конструктор".
		personal_account_constructor = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.WAIT_PAGE_CONSTRUCTOR))).text
		assert personal_account_constructor == 'Соберите бургер'



	def test_from_your_personal_account_click_logo_stellarburger(self, go_to_personal_account): # Переход из профиля личного кабинета в конструктор по клику лого "Stellar Burger"
		driver = go_to_personal_account
		driver.find_element(*Locator.CLICK_PERSONAL_AREA_HOME_PAGE).click()  # Клик по кнопке "Личный кабинет на главной странице"
		WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.WAIT_LABEL_PROFILE)))  # Явное ожидание загрузки формы личного кабинета
		driver.find_element(*Locator.CLICK_LOGO_STELLAR_BURGER).click()                                 # клик по лого "Stellar Burger"
		personal_account_constructor = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locator.WAIT_PAGE_CONSTRUCTOR))).text
		assert personal_account_constructor == 'Соберите бургер'

