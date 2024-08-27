from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class ContactUsPage(Page):
    USE_THIS_EMAIL_TEXT = By.CSS_SELECTOR, ".text-span-37"

    def verify_right_page_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def verify_text_present(self, expected_text):
        self.verify_text(expected_text, self.USE_THIS_EMAIL_TEXT)
