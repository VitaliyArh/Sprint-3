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








# from locator import Locator
#
# class TestSectionConctructor:
#
# 	def test_go_to_buns_section(self, driver):
# 		driver.find_element(*Locator.CLICK_BUTTON_SAUCES).click()
# 		driver.find_element(*Locator.CLICK_BUTTON_BULKA).click()
# 		name_buns = driver.find_element(*Locator.PASSED_BULKA_SECTION).text
# 		assert name_buns == 'Булки'
#
# 	def test_go_to_sauces_section(self, driver):
# 		driver.find_element(*Locator.CLICK_BUTTON_STUFFING).click()
# 		driver.find_element(*Locator.CLICK_BUTTON_SAUCES).click()
# 		name_sauces = driver.find_element(*Locator.PASSED_SAUCES_SECTION).text
# 		assert name_sauces == 'Соусы'
#
# 	def test_go_to_stuffing_section(self, driver):
# 		driver.find_element(*Locator.CLICK_BUTTON_STUFFING).click()
# 		name_stuffing = driver.find_element(*Locator.PASSED_STUFFING_SECTION).text
# 		assert name_stuffing == 'Начинки'
















