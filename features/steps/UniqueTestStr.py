from behave import *
from lab_python_fp.unique import Unique


# Implementation for string lists
@given("the list is [{list}] and ignore case param is {ignore_case}")
def have_info(context, list, ignore_case):
    print(list)
    context.list = [i for i in list.split(', ')]
    context.ignore_case = ignore_case


@when("I find unique")
def find_unique(context):
    context.result = list(Unique(context.list, ignore_case=context.ignore_case).__next__())


@then("I expect the result to be [{list}]")
def expect_result(context, list):
    result = [i for i in list.split(', ')]
    print(context.ignore_case)
    print(result, context.result)
    assert context.result == result


# Implementation for nums lists
# @given("I have list {list:g*}")
# def have_info(step, list):
# step.context.list =
# @given('I have list ["A", "a", "a", "A", "B", "b", "B", "B"] and ignore case param is False')
# def step_impl(context):
#     raise NotImplementedError(
#         STEP: Given I have list ["A", "a", "a", "A", "B", "b", "B", "B"] and ignore case param is False')
#
#
# @given('I have list ["A", "a", "a", "B", "a", "B", "b", "A"] and ignore case param is True')
# def step_impl(context):
#     raise NotImplementedError(
#         u'STEP: Given I have list ["A", "a", "a", "B", "a", "B", "b", "A"] and ignore case param is True')
