from radish import given, when, then

# Implementation for string lists
@given("I have list [{list:w*}] and ignore case param is {ignore_case:Boolean}")
def have_info(step, list, ignore_case):
    step.context.list = list
    step.context.ignore_case = ignore_case

@when("I find unique")
def find_unique(step):
    step.context.unique.add_data(step.context.list)
    step.context.unique.add_ignore_case(step.context.ignore_case)

    step.context.result = step.context.unique.__next__()

@then("I expect the result to be {result:w*}")
def expect_result(step, result):
    assert step.context.result == result


# Implementation for nums lists
# @given("I have list {list:g*}")
# def have_info(step, list):
    # step.context.list =

