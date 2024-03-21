from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MenuBlock(Page):

    # SETTINGS_BTN = (By.CSS_SELECTOR, ".menu_block_1 [href*='settings']")
    SETTINGS_BTN = (By.XPATH, "//a[contains(@href, '/settings') and contains(., 'Settings')]")

    def click_settings(self):
        sleep(50)
        self.wait.until(EC.visibility_of_element_located(self.SETTINGS_BTN), f"Element is not visible")
        self.wait_element_clickable_click(*self.SETTINGS_BTN)
