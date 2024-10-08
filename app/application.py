from pages.base_page import Page
from pages.add_a_project_page import AddAProjectPage
from pages.contact_us_page import ContactUsPage
from pages.main_page import MainPage
from pages.menu_block import MenuBlock
from pages.settings_profile_page import SettingsProfilePage
from pages.sign_in_page import SignInPage
from pages.sign_up_page import SignUpPage


class Application:
    def __init__(self, driver):
        self.pages = Page(driver)
        self.add_a_project_page = AddAProjectPage(driver)
        self.contact_us_page = ContactUsPage(driver)
        self.main_page = MainPage(driver)
        self.menu_block = MenuBlock(driver)
        self.settings_profile_page = SettingsProfilePage(driver)
        self.sign_in_page = SignInPage(driver)
        self.sign_up_page = SignUpPage(driver)
