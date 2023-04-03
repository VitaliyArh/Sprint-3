from locator import Locator

class TestSectionConctructor:

	def test_go_to_buns_section(self, driver):
		driver.find_element(*Locator.CLICK_BUTTON_SAUCES).click()
		driver.find_element(*Locator.CLICK_BUTTON_BULKA).click()
		name_food = driver.find_element(*Locator.NAME_FOOD).text
		assert name_food == 'Булки'

	def test_go_to_sauces_section(self, driver):
		driver.find_element(*Locator.CLICK_BUTTON_STUFFING).click()
		driver.find_element(*Locator.CLICK_BUTTON_SAUCES).click()
		name_food = driver.find_element(*Locator.NAME_FOOD).text
		assert name_food == 'Соусы'

	def test_go_to_stuffing_section(self, driver):
		driver.find_element(*Locator.CLICK_BUTTON_STUFFING).click()
		name_food = driver.find_element(*Locator.NAME_FOOD).text
		assert name_food == 'Начинки'
