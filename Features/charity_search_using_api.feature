Feature: Check for charities in charity list of TradeMe

  Scenario: Check for an existing charity in charity list
    Given I send get request to TradeME for Charity list
    When The response is: 200
    Then I check for: St John charity in the charity list