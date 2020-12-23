"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
uniques = {}
count_uniques = 0

def add_phone_number(num):
    global uniques
    global count_uniques
    if not num in uniques:
        uniques[num] = True
        count_uniques += 1

def traverse_columns(stop_index, array):
    for i in range(stop_index):
        add_phone_number(array[i][0])
        add_phone_number(array[i][1])               

traverse_columns(len(calls)-1, calls)
traverse_columns(len(texts)-1, texts)

print("There are " + str(count_uniques) + " different telephone numbers in the records.")
