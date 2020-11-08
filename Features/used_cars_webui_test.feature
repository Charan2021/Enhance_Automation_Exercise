Feature: Validate displayed details of used cars

  Scenario: Check website connection status and query car details
    Given I launch the browser: Google
    When  The webpage: https://www.tmsandbox.co.nz is reachable
    Then  I query for used cars listing and its details

  Scenario Outline: Validate if car details has <info> information
    Given I launch the browser: Google
    When  The webpage: https://www.tmsandbox.co.nz is reachable
    Then  I query for used cars listing and its details
    And I check for: <info> information

    Examples:
      | info |
      | Number plate |
      | Kilometres   |
      | Body         |
      | Seats        |