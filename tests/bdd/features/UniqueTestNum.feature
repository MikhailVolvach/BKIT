Feature: Test of unique.py with number list
  descr

  Scenario: unique.py test with numbers 1
    Given I have list [1, 2, 1, 1, 3, 2, 1, 2]
    When I find unique
    Then I expect the result to be [1, 2, 3]
