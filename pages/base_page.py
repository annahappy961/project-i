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
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator),
                f"Element by {locator} is not found"
            )
            element.send_keys(text)
            logger.info(f"Input text '{text}' into element with locator {locator}")
        except StaleElementReferenceException:
            # If element reference becomes stale, locate the element again
            element = self.wait.until(
                EC.visibility_of_element_located(locator),
                f"Stale element reference: Element by {locator} is not found"
            )
            element.send_keys(text)
            logger.info(f"Input text '{text}' into element with locator {locator} after stale reference")

    def get_input_value(self, locator):
        get_attribute = self.driver.find_element(*locator).get_attribute("value")
        logger.info(f"Get input value '{get_attribute}' from element with locator {locator}")
        return get_attribute

    def wait_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} is not clickable"
        )
        logger.info(f"Element with locator {locator} is clickable")

    def wait_element_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} is not clickable"
        ).click()
        logger.info(f"Clicked on element with locator {locator}")

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, \
            f"Expected {expected_partial_url} not in {actual_url}"
        logger.info(f"Verified partial URL: Expected '{expected_partial_url}' found in actual URL: '{actual_url}'")
