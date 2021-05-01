import pandas as pd
import pm4py


def import_csv(file_path):
    event_log = pd.read_csv(file_path, sep=';')
    event_log = pm4py.format_dataframe(event_log, case_id='case_id', activity_key='activity', timestamp_key='timestamp')
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))


if __name__ == "__main__":
    import_csv("/Users/lukasjunger/PycharmProjects/pm4py_gettting_started/venv/data/running-example.csv")