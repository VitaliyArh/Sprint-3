import pytest
from data import Data
from locator import Locator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Chrome(options=options)
    browser.get(Data.URL)

    yield browser
    browser.quit()

@pytest.fixture(scope = 'function')
def go_to_personal_account(driver):
    driver.find_element(*Locator.CLICK_PERSONAL_AREA_HOME_PAGE).click()
    driver.find_element(*Locator.ENTER_EMAIL_1).send_keys(Data.VALID_EMAIL)
    driver.find_element(*Locator.ENTER_PASSWORD).send_keys(Data.VALID_PASSWORD)
    driver.find_element(*Locator.CLICK_BUTTON_TO_COME_IN).click()
    return driver
