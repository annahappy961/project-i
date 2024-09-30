Feature: Feature testing

#  Scenario: User can add a project through the settings
#    Given Open Sign In page https://soft.reelly.io/sign-in
#    When Log in to the existing account: and
#    When Click on settings option
#    And Click on Add a project
#    Then Verify URL has add-a-project
#    When Add your name as test16, phone as 123, email as test16@gmail.com to the respective fields
#    Then Verify the correct information is present in the input fields
#    And  Verify “Send an application” button is available and clickable

#  Scenario: User can open the Contact us page
#    Given Open Main page https://soft.reelly.io
#    When Log in to the existing account:
#    When Click on settings option
#    When Click on Contact Us
#    Then Verify URL has contact-us
#    And Verify Use this email: is seen

#  Scenario: User can click on “Connect the company” on the left side of the main page
#    Given Open Main page https://soft.reelly.io
#    When Log in to the existing account:
#    And Click on “Connect the company” and switch the new tab
#    Then Verify connect the company URL has book-presentation

  Scenario: User can go to settings and edit the personal information
    Given Open Main page https://soft.reelly.io
    When Log in to the existing account:
    And Click on settings option
    And Click on Edit profile option
    And Enter the English language in the Languages input field
    Then Verify the right language is present in the input field: English
    And Verify “Close” and “Save Changes” buttons are available and clickable
