from pages.base_page import Page
from pages.add_a_project_page import AddAProjectPage
from pages.main_page import MainPage
from pages.menu_block import MenuBlock
from pages.settings_profile_page import SettingsProfilePage


class Application:
    def __init__(self, driver):
        self.pages = Page(driver)
        self.main_page = MainPage(driver)
        self.menu_block = MenuBlock(driver)
        self.settings_profile_page = SettingsProfilePage(driver)
        self.add_a_project_page = AddAProjectPage(driver)
