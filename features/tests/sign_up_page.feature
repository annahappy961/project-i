Feature: Sign Up Test

#   Scenario: User can enter the information into the input fields on the registration page
#     Given Open Sign Up page
#     When Enter details into the required fields on the sign up page
#     Then Verify the system displays the entered details exactly as provided
#
  Scenario Outline: User can enter the information into the input fields on the registration page
    Given Open the Sign Up page https://soft.reelly.io/sign-up
    When Enters details into the required fields on the sign up page with <fullname>, <phone>, <email>, <password>, <website>, <role>, <position>, <country>, <company_size>
    Then Verify the system displays the entered details exactly as provided with <fullname>, <phone>, <email>, <password>, <website>, <role>, <position>, <country>, <company_size>

    Examples:
      | fullname       | phone     | email          | password      | website  | role      | position         | country                  | company_size |
      | Test Full Name | 999999999 | test@gmail.com | Password:Test | test.com | Developer | Seller / Manager | United States of America | 50-100       |
