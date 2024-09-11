from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    USERNAME_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[class*='login-button']")

    def open_sign_in_page(self, url):
        self.open(url)

    def log_in_to_existing_account(self, username, password):
        self.input_text(username, *self.USERNAME_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.wait_element_clickable_click(*self.CONTINUE_BTN)
