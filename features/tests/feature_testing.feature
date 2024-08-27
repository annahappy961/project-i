Feature: Feature testing

  Scenario: User can add a project through the settings
    Given Open Sign In page https://soft.reelly.io/sign-in
    When Log in to the existing account: zarubina.anna.qa@gmail.com and WubNv92HAuZ3Xk!
    When Click on settings option
    And Click on Add a project
    Then Verify URL has add-a-project
    When Add your name as test16, phone as 123, email as test16@gmail.com to the respective fields
    Then Verify the correct information is present in the input fields
    And  Verify “Send an application” button is available and clickable

  Scenario: User can open the Contact us page
    Given Open Main page https://soft.reelly.io
    When Log in to the existing account: zarubina.anna.qa@gmail.com and WubNv92HAuZ3Xk!
    When Click on settings option
    When Click on Contact Us
    Then Verify URL has contact-us
    And Verify Use this email: is seen


