import pandas as pd
import pm4py
import datetime as dt
import graphviz


if __name__ == "__main__":
    log = pm4py.read_xes("/Users/lukasjunger/PycharmProjects/pm4py_gettting_started/venv/data/running-example.xes")

    process_tree = pm4py.discover_process_tree_inductive(log)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn_model)

    pm4py.view_process_tree(process_tree)


# Symbole werden hier teilweise nicht dargestellt.
# z.B.: "seq" statt "->" / "and" statt "+" / "XOR" statt "X"

# Außerdem erscheint der Hintergrund gräulich und nicht weiß.
