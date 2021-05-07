import pandas as pd
import pm4py
import datetime as dt
import graphviz


if __name__ == "__main__":
    log = pm4py.read_xes("/Users/lukasjunger/PycharmProjects/pm4py_gettting_started/venv/data/running-example.xes")

    dfg, start_activities, end_activities = pm4py.discover_dfg(log)
    pm4py.view_dfg(dfg, start_activities, end_activities)

    map = pm4py.discover_heuristics_net(log)
    pm4py.view_heuristics_net(map)
