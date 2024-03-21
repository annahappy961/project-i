from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from support.logger import logger


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open(self, url):
        logger.info(f'Opening url {url}...')
        self.driver.get(url)

    def find_element(self, *locator):
        logger.info(f'Search for element {locator}')
        return self.driver.find_element(*locator)

    def input_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    def get_input_value(self, locator):
        get_attribute = self.driver.find_element(*locator).get_attribute("value")
        return get_attribute

    def wait_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} is not clickable"
        )

    def wait_element_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} is not clickable"
        ).click()

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, \
            f"Expected {expected_partial_url} not in {actual_url}"
