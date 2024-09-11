from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class ConnectTheCompanyTab(Page):
    CONNECT_THE_COMPANY_BTN = (By.CSS_SELECTOR, "[class ='get-free-period menu']")

    def click_connect_the_company_and_switch_to_new_tab(self):
        self.switch_to_new_tab(*self.CONNECT_THE_COMPANY_BTN)

    def verify_connect_the_company_tab_partial_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)
