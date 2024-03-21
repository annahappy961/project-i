from selenium.webdriver.common.by import By

from pages.base_page import Page


class SettingsProfilePage(Page):
    ADD_PROJECT_LINK_TEXT = (By.CSS_SELECTOR, "[class*='block-menu'] [href*='project']")

    def click_add_project(self):
        self.wait_element_clickable_click(*self.ADD_PROJECT_LINK_TEXT)
