from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignUpPage(Page):
    FIRS_LAST_NAME_FIELD = (By.ID, "Full-Name")
    PHONE_FIELD = (By.ID, "phone2")
    EMAIL_FIELD = (By.ID, "Email-3")
    PASSWORD_FIELD = (By.ID, "field")
    COMPANY_WEBSITE_FIELD = (By.ID, "Company-website")
    ROLE_DROPDOWN = (By.ID, "Role")
    POSITION_DROPDOWN = (By.ID, "Position")
    COUNTRY_DROPDOWN = (By.ID, "country-select")
    COMPANY_SIZE_DROPDOWN = (By.ID, "Agents-amount-2")
    READ_ACCEPT_CHECKBOX = (By.ID, "checkbox")

    def open_sign_up_page(self):
        self.open(" https://soft.reelly.io/sign-up")

    # def enter_information_into_input_fields(self):
    #     self.input_text("Test Full Name", *self.FIRS_LAST_NAME_FIELD)
    #     self.input_text("999999999", *self.PHONE_FIELD)
    #     self.input_text("test@gmail.com", *self.EMAIL_FIELD)
    #     self.input_text("Password:Test", *self.PASSWORD_FIELD)
    #     self.input_text("test.com", *self.COMPANY_WEBSITE_FIELD)
    #     self.select_dropdown_value("Developer", *self.ROLE_DROPDOWN)
    #     self.select_dropdown_value("Seller / Manager", *self.POSITION_DROPDOWN)
    #     self.select_dropdown_value("United States of America", *self.COUNTRY_DROPDOWN)
    #     self.select_dropdown_value("50-100", *self.COMPANY_SIZE_DROPDOWN)
    #     self.checkbox_click(*self.READ_ACCEPT_CHECKBOX)
    #
    # def verify_details_display_correctly(self):
    #     self.verify_element_value("Test Full Name", *self.FIRS_LAST_NAME_FIELD)
    #     self.verify_element_value("999999999", *self.PHONE_FIELD)
    #     self.verify_element_value("test@gmail.com", *self.EMAIL_FIELD)
    #     self.verify_element_value("Password:Test", *self.PASSWORD_FIELD)
    #     self.verify_element_value("test.com", *self.COMPANY_WEBSITE_FIELD)
    #     self.get_dropdown_value("Developer", *self.ROLE_DROPDOWN)
    #     self.get_dropdown_value("Seller / Manager", *self.POSITION_DROPDOWN)
    #     self.get_dropdown_value("United States of America", *self.COUNTRY_DROPDOWN)
    #     self.get_dropdown_value("50-100", *self.COMPANY_SIZE_DROPDOWN)
    #     self.is_checkbox_selected(*self.READ_ACCEPT_CHECKBOX)

    def enter_information_into_input_fields(self, fullname, phone, email, password, website, role, position, country,
                                            company_size):
        self.input_text(fullname, *self.FIRS_LAST_NAME_FIELD)
        self.input_text(phone, *self.PHONE_FIELD)
        self.input_text(email, *self.EMAIL_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.input_text(website, *self.COMPANY_WEBSITE_FIELD)
        self.select_dropdown_value(role, *self.ROLE_DROPDOWN)
        self.select_dropdown_value(position, *self.POSITION_DROPDOWN)
        self.select_dropdown_value(country, *self.COUNTRY_DROPDOWN)
        self.select_dropdown_value(company_size, *self.COMPANY_SIZE_DROPDOWN)
        self.checkbox_click(*self.READ_ACCEPT_CHECKBOX)

    def verify_details_display_correctly(self, fullname, phone, email, password, website, role, position, country,
                                         company_size):
        assert self.get_input_value(
            self.FIRS_LAST_NAME_FIELD) == fullname, f"Verification Failed for full name, expected {fullname}"
        assert self.get_input_value(self.PHONE_FIELD) == phone, f"Verification Failed for phone, expected {phone}"
        assert self.get_input_value(self.EMAIL_FIELD) == email, f"Verification Failed for email, expected {email}"
        assert self.get_input_value(
            self.PASSWORD_FIELD) == password, f"Verification Failed for password, expected {password}"
        assert self.get_input_value(
            self.COMPANY_WEBSITE_FIELD) == website, f"Verification Failed for website, expected {website}"

        assert self.get_dropdown_value(*self.ROLE_DROPDOWN) == role, f"Verification Failed for role, expected {role}"
        assert self.get_dropdown_value(
            *self.POSITION_DROPDOWN) == position, f"Verification Failed for position, expected {position}"
        assert self.get_dropdown_value(
            *self.COUNTRY_DROPDOWN) == country, f"Verification Failed for country, expected {country}"
        assert self.get_dropdown_value(
            *self.COMPANY_SIZE_DROPDOWN) == company_size, f"Verification Failed for company size, expected {company_size}"

        self.is_checkbox_selected(*self.READ_ACCEPT_CHECKBOX)
