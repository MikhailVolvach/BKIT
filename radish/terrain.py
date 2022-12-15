from radish import before, after

import lab_python_fp.unique as unique

@before.each_scenario
def init_unique(scenario):
    scenario.context.unique = unique.Unique()

@after.each_scenario
def destroy_unique(scenario):
    del scenario.context.unique

