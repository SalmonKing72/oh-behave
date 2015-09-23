@testing
Feature: showing off behave with selenium

Scenario: test a web app
  Given we have behave installed
  When I visit google
  Then it should have a title "Google"