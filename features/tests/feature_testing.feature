Feature: Feature testing

  Scenario: User can add a project through the settings
    Given Open Sign In page
    When Log in to the existing account:  and 
    When Click on settings option
    And Click on Add a project
    Then Verify URL has add-a-project
    When Add your name as test16, phone as 123, email as test16@gmail.com to the respective fields
    Then Verify the correct information is present in the input fields
    And  Verify “Send an application” button is available and clickable
