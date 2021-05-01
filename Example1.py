import pandas as pd

def import_csv(file_path):
    event_log = pd.read_csv(file_path, sep=';')
    num_events = len(event_log)
    num_cases = len(event_log.case_id.unique())
    print("Number of events: {}\nNumber of cases: {}".format(num_events, num_cases))


if __name__ == "__main__":
    import_csv("/Users/lukasjunger/PycharmProjects/pm4py_gettting_started/venv/data/running-example.csv")