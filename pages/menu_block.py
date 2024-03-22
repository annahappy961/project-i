from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import Page


class MenuBlock(Page):
    SETTINGS_BTN = (By.CSS_SELECTOR, ".menu_block_1 [href*='settings']")

    def click_settings(self):
        self.wait_element_clickable_click(*self.SETTINGS_BTN)
