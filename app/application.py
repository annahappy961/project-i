from pages.base_page import Page
from pages.add_a_project_page import AddAProjectPage
from pages.menu_block import MenuBlock
from pages.settings_profile_page import SettingsProfilePage
from pages.sign_in_page import SignInPage


class Application:
    def __init__(self, driver):
        self.pages = Page(driver)
        self.add_a_project_page = AddAProjectPage(driver)
        self.menu_block = MenuBlock(driver)
        self.settings_profile_page = SettingsProfilePage(driver)
        self.sign_in_page = SignInPage(driver)
