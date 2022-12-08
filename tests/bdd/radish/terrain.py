from radish import before, after

from lab_python_fp import Unique

@before.each_scenario
def init_unique(scenario):
    scenario.context.unique = Unique()

@after.each_scenario
def destroy_unique(scenario):
    del scenario.context.unique

