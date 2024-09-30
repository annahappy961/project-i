from behave import given, when, then


# @given('Open sign up page')
# def open_sign_up_page(context):
#     context.app.sign_up_page.open_sign_up_page()
#
#
# @when('Enter details into the required fields on the sign up page')
# def enter_information_into_input_fields(context):
#     context.app.sign_up_page.enter_information_into_input_fields()
#
#
# @then('Verify the system displays the entered details exactly as provided')
# def verify_information_in_input_fields(context):
#     context.app.sign_up_page.verify_details_display_correctly()


@given('Open the Sign up page {url}')
def open_sign_up_page(context, url):
    context.app.sign_up_page.open_sign_up_page(url)


@when(
    'Enters details into the required fields on the sign up page with {fullname}, {phone}, {email}, {password}, {website}, {role}, {position}, {country}, {company_size}')
def enter_information_into_input_fields(context, fullname, phone, email, password, website, role, position, country,
                                        company_size):
    context.app.sign_up_page.enter_information_into_input_fields(fullname, phone, email, password, website, role,
                                                                 position, country, company_size)


@then(
    'Verify the system displays the entered details exactly as provided with {fullname}, {phone}, {email}, {password}, {website}, {role}, {position}, {country}, {company_size}')
def verify_information_in_input_fields(context, fullname, phone, email, password, website, role, position, country,
                                       company_size):
    context.app.sign_up_page.verify_details_display_correctly(fullname, phone, email, password, website, role, position,
                                                              country, company_size)
