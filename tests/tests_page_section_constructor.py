# тесты страницы раздел конструктор
# Булки, Соусы, Начинки

from selenium.webdriver.common.by import By
from locator import Locator

class TestSectionConctructor:

	def test_go_to_buns_section(self, driver):                                   # переход в раздел "Булки" в конструкторе
		driver.find_element(*Locator.CLICK_BUTTON_SAUCES).click()                # кликнули на "Соусы"
		driver.find_element(*Locator.CLICK_BUTTON_BULKA).click()                 # кликнули на "Булки"
		name_buns = driver.find_element(*Locator.PASSED_BULKA_SECTION).get_attribute('class')
		assert name_buns == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"



	def test_go_to_sauces_section(self, driver):                                    # переход в раздел "Соусы"
		driver.find_element(*Locator.CLICK_BUTTON_STUFFING).click()                 # кликнули на "Начинки"
		driver.find_element(*Locator.CLICK_BUTTON_SAUCES).click()                   # кликнули на "Соусы"
		name_sauces = driver.find_element(*Locator.PASSED_SAUCES_SECTION).get_attribute('class')
		assert name_sauces == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"



	def test_go_to_stuffing_section(self, driver):                                     # переход в раздел "Начинки"
		driver.find_element(*Locator.CLICK_BUTTON_STUFFING).click()                    # кликнули на "Начинки"
		name_stuffing = driver.find_element(*Locator.PASSED_STUFFING_SECTION).get_attribute("class")
		assert name_stuffing == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"










