import pandas as pd
import pm4py
import datetime as dt


if __name__ == "__main__":
    log = pm4py.read_xes("/Users/lukasjunger/PycharmProjects/pm4py_gettting_started/venv/data/running-example.xes")


#Loop um log-file zu durchsuchen und alle activities in einem dict zu speichern, welche ein trace starten.
    # d = dict()
    # for t in log:
    #    d[t[0]['concept:name']] = d[t[0]['concept:name']] + 1 if t[0]['concept:name'] in d else 1



### Anwendung von verschiedensten Basic- Filtern

#filtered1: Durchsucht das log-file nach Events vom Typ 'register request' die eine start-activity sind
    filtered1 = pm4py.filter_start_activities(log, {'register request'})

#filtered2: Da es keine activity gibt mit dem Namen 'register request TYPO!' Wird Null traces wiedergeben.
    filtered2 = pm4py.filter_start_activities(log, {'register request TYPO!'})

#filtered3: Same same wie filtered1, nur im Bezug auf end-activities. Gibt alle traces wieder welche mit 'pay compensation' enden.
    filtered3 = pm4py.filter_end_activities(log, 'pay compensation')

#Event-Attribute-Filter
# filtered4: Attribute-Filter bzgl. 'org:resource', welche Pete und/oder Mike enthalten. Hier levels='cases'.
# Result: Jegliche traces, welche einen Event enthalten, bei denen die Attribut-Bedingung Pete oder Mike zutrifft.
    filtered4 = pm4py.filter_event_attribute_values(log, 'org:resource', {'Pete', 'Mike'})

#filtered5: Unterschied zu filtered4: Alle Events, welche nicht die Attribut-Bedingung erfüllen, werden removed.
    filtered5 = pm4py.filter_event_attribute_values(log, 'org:resource', {'Pete', 'Mike'}, level='event')

# Trace-Attribute-Filter
#filtered6: Filtered das log-file nach dem Attribute-Value & removed alle traces, welche nicht die Bedingung erfüllen.
    filtered6 = pm4py.filter_trace_attribute_values(log, 'concept:name', {'3', '4'})

# filtered7: Negation des Filters. Alle Traces welche die Bedingung erfüllen, werden removed.
    filtered7 = pm4py.filter_trace_attribute_values(log, 'concept:name', {'3', '4'}, retain=False)

#Filtering Trace Variants.

# Gibt alle Varianten wieder, die sich in der Log-Datei befinden.
vars = pm4py.get_variants(log)
#for k, v in vars.items():
#    print(k)
#    print(v)

#filtered8: Filter for a specific variant. Log-file wird nach traces durchsucht, bei denen die Events in dieser Reihenfolge stattfinden.
filtered8 = pm4py.filter_variants(log, [['register request', 'check ticket', 'examine casually', 'decide', 'pay compensation']])

#Filtering Directly/Eventually-Follows:
#filtered9: Show all traces, where 'check ticket' is followed directly by 'examine casually'
filtered9 = pm4py.filter_directly_follows_relation(log, [('check ticket', 'examine casually')])

#filtered10: Same as filter above, but the event just has to eventually follow the previous one.
filtered10 = pm4py.filter_directly_follows_relation(log, [('check ticket', 'examine casually')])

#Filtering on Time
#filtered11: Cuts of the events from a trace, which are not within this time-range
filtered11 = pm4py.filter_time_range(log, dt.datetime(2010, 12, 30), dt.datetime(2010, 12, 31), mode='events')

#filtered12: The traces in the list are completely within the time-range
filtered12 = pm4py.filter_time_range(log, dt.datetime(2010, 12, 30), dt.datetime(2010, 12, 31), mode='traces_contained')

#filtered13: Every trace which has an event within the time-range is relevant
filtered13 = pm4py.filter_time_range(log, dt.datetime(2010, 12, 30), dt.datetime(2010, 12, 31), mode='traces_intersecting')

print('Hi Debugger')










