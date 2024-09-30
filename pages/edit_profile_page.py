from selenium.webdriver.common.by import By

from pages.base_page import Page


class EditProfilePage(Page):
    LANGUAGES_FIELD = (By.ID, "Languages")
    CLOSE_BTN = (By.CSS_SELECTOR, "[class='profile-button-block'] [class*='close-button']")
    SAVE_CHANGES_BTN = (By.CSS_SELECTOR, "[class='profile-button-block'] [wized='saveButtonProfile']")

    def enter_language(self, language):
        self.input_text(language, *self.LANGUAGES_FIELD)

    def verify_language_displayed(self, language):
        assert self.get_input_value(
            self.LANGUAGES_FIELD) == language, f"Verification Failed for language, expected {language}"

    def verify_close_button_clickable(self, *locator):
        self.wait_element_clickable(*self.CLOSE_BTN)

    def verify_save_changes_button_clickable(self, *locator):
        self.wait_element_clickable(*self.SAVE_CHANGES_BTN)
