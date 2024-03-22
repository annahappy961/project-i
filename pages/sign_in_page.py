from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    USERNAME_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[class*='login-button']")

    def open_sign_in_page(self):
        self.open('https://soft.reelly.io/sign-in')

    def log_in_to_existing_account(self, username, password):
        self.input_text(self.USERNAME_FIELD, username)
        self.input_text(self.PASSWORD_FIELD, password)
        self.wait_element_clickable_click(*self.CONTINUE_BTN)
