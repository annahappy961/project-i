from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SettingsProfilePage(Page):
    ADD_PROJECT_LINK_TEXT = (By.CSS_SELECTOR, "[class*='block-menu'] [href*='project']")
    CONTACT_US_LINK_TEXT = (By.CSS_SELECTOR, ".settings-block-menu [href='/contact-us']")
    EDIT_PROFILE = (By.CSS_SELECTOR, "[href='/profile-edit']")

    def click_add_project(self):
        sleep(10)
        self.wait_element_clickable_click(*self.ADD_PROJECT_LINK_TEXT)

    def click_contact_us(self):
        self.wait_element_clickable_click(*self.CONTACT_US_LINK_TEXT)

    def click_edit_profile(self):
        self.wait_element_clickable_click(*self.EDIT_PROFILE)
