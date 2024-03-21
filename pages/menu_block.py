from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MenuBlock(Page):

    # SETTINGS_BTN = (By.CSS_SELECTOR, ".menu_block_1 [href*='settings']")
    SETTINGS_BTN = (By.XPATH, "//a[contains(@href, '/settings') and contains(., 'Settings')]")

    def click_settings(self):
        sleep(5)
        self.wait_element_clickable_click(*self.SETTINGS_BTN)
