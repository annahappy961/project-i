from behave import given, when, then


@given("Open Sign In page")
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when("Log in to the existing account: {username} and {password}")
def login_to_existing_account(context, username, password):
    context.app.sign_in_page.log_in_to_existing_account(username, password)


@when("Click on settings option")
def click_settings(context):
    context.app.menu_block.click_settings()


@when("Click on Add a project")
def click_add_project(context):
    context.app.settings_profile_page.click_add_project()


@then("Verify URL has {expected_part_url}")
def verify_right_page_url(context, expected_part_url):
    context.app.add_a_project_page.verify_right_page_url(expected_part_url)


@when("Add your name as {name}, phone as {phone_number}, email as {email} to the respective fields")
def add_test_information(context, name, phone_number, email):
    context.app.add_a_project_page.add_test_information(name, phone_number, email)


@then("Verify the correct information is present in the input fields")
def verify_test_information_entered_correct(context):
    expected_values = {
        "Your-name": "test16",
        "Phone": "123",
        "Email-add-project": "test16@gmail.com"
    }
    context.app.add_a_project_page.verify_test_information_entered_correct(expected_values)


@then("Verify “Send an application” button is available and clickable")
def verify_application_button_clickable(context):
    context.app.add_a_project_page.verify_application_button_clickable()
