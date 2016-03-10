@testing
Feature: showing off behave with selenium

Scenario: test a web app
  Given we have behave installed
  When I visit devcorr
  Then it should have a title "Devcorr"
  And I should see the contact button