Feature: Test of unique.py with number list
  descr

  Scenario: UniqueTestNum.py
    Given the list is [1, 2, 1, 1, 3, 2, 1, 2]
    When I find unique
    Then I expect the result to be [1, 2, 3]
