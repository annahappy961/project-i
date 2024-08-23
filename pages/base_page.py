from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
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

    def checkbox_click(self, *locator):
        checkbox_element = self.driver.find_element(*locator)
        if not checkbox_element.is_selected():
            checkbox_element.click()

    def input_text(self, text, *locator):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator),
                f"Element by {locator} is not found"
            )
            element.clear()
            element.send_keys(text)
            logger.info(f"Input text '{text}' into element with locator {locator}")
        except TimeoutException as e:
            logger.error(f"Timeout waiting for element by {locator}: {str(e)}")
        except StaleElementReferenceException as e:
            logger.error(f"Stale element by {locator}: {str(e)}")
            # Optionally retry once if the element goes stale
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)

    def select_dropdown_value(self, value, *locator):
        try:
            select_element = self.find_element(*locator)
            select = Select(select_element)
            select.select_by_visible_text(value)
            logger.info(f"Selected '{value}' from dropdown with locator {locator}")
        except NoSuchElementException as e:
            logger.error(f"Dropdown not found by {locator}: {str(e)}")
        except ElementNotVisibleException as e:
            logger.error(f"Dropdown not visible by {locator}: {str(e)}")

    def get_input_value(self, locator):
        get_attribute = self.driver.find_element(*locator).get_attribute("value")
        logger.info(f"Get input value '{get_attribute}' from element with locator {locator}")
        return get_attribute

    def get_dropdown_value(self, *locator):
        # Locate the dropdown element and create a Select object.
        try:
            # Attempt to find the dropdown element and create a Select object
            select_element = self.find_element(*locator)
            select = Select(select_element)
            return select.first_selected_option.text
        except NoSuchElementException as e:
            # Raise an error with detailed info about the failed locator
            raise NoSuchElementException(f"No element found with locator {locator}. Error: {e}")
        except Exception as e:
            # Catch other exceptions that may occur, potentially related to Select handling
            raise Exception(f"An error occurred while trying to retrieve the dropdown value: {e}")

    def wait_element_clickable(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(*locator),
            message=f"Element by {locator} is not clickable"
        )
        logger.info(f"Element with locator {locator} is clickable")

    def wait_element_clickable_click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} not clickable"
        ).click()
        logger.info(f"Clicked on element with locator {locator}")

    def is_checkbox_selected(self, *locator):
        checkbox_element = self.driver.find_element(*locator)
        assert checkbox_element.is_selected() == True, f"Checkbox needs to selected!"

    def verify_element_value(self, expected_value, *locator):
        try:
            element = self.driver.find_element(*locator)
            actual_value = element.get_attribute("value")
            assert actual_value == expected_value, f"Expected value '{expected_value}', but got '{actual_value}'"
            logger.info(f"Verified value '{actual_value}' on element with locator {locator}")
        except AssertionError as e:
            logger.error(f"Assertion error: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error verifying value on element with locator {locator}: {str(e)}")
            raise

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, \
            f"Expected {expected_partial_url} not in {actual_url}"
        logger.info(f"Verified partial URL: Expected '{expected_partial_url}' found in actual URL: '{actual_url}'")
