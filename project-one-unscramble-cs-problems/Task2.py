"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# assign names to columns in the csv file
sender = 0
receiver = 1
duration = 3
# keep track of total call durations
durations = {}

for call in calls:
    caller = call[sender]
    callee = call[receiver]
    #typecast hash value to int to allow arithmetic calculations
    if caller in durations:
        durations[caller] += int(call[duration])
    else:
        durations[caller] = int(call[duration])

    if callee in durations:
        durations[callee] += int(call[duration])
    else:
        durations[callee] = int(call[duration])

#retrieve max values from durations mapping
max_duration = max(durations.values())
# I used this resource for the two lines below: https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
position = durations.values().index(max_duration)
max_number = durations.keys()[position]

print(max_number + " spent the longest time, " + str(max_duration) + " seconds, on the phone during September 2016")
