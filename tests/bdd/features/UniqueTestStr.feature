Feature: Test of unique.py with string lists
  Description of the feature

  Scenario: unique.py test 1
    Given I have list ["A", "a", "a", "A", "B", "b", "B", "B"] and ignore case param is False
    When I find unique
    Then I expect the result to be ["A", "B"]

  Scenario: unique.py test 3
    Given I have list ["A", "a", "a", "B", "a", "B", "b", "A"] and ignore case param is True
    When I find unique
    Then I expect the result to be ["A", "a", "B", "b"]

