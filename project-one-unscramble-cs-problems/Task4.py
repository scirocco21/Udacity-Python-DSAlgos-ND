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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
#use hash data structure to keep track of previous numbers
callers = {}
# assign names to columns in the csv file
sender = 0
receiver = 1
#log all unique callers
for call in calls:
  if not call[sender] in callers:
    callers[call[sender]] = True
#remove any callers that don't look like telemarketers
for call in calls:
  if call[receiver] in callers:
    del callers[call[receiver]]
for text in texts:
  if text[receiver] in callers:
    del callers[text[receiver]]
  elif text[sender] in callers:
    del callers[text[sender]]

print("These numbers could be telemarketers: ")
print(*sorted(callers), sep="\n")