Feature: Test of unique.py with string lists
  Description of the feature

  Scenario: unique.py test 1
    Given the list is [A, a, a, B, a, B, b, A] and ignore case param is False
    When I find unique
    Then I expect the result to be [A, a, B, b]

  Scenario: unique.py test 2
    Given the list is [A, a, a, B, a, B, b, A] and ignore case param is True
    When I find unique
    Then I expect the result to be [A, B]

