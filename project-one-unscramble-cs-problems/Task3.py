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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# PART A
# assign names to columns in the csv file
sender = 0
receiver = 1
#use hash table for quick look ups
unique_codes = {}
#helper methods to determine type of receiver number
def has_area_code(num):
  return num[0] == "("

def has_mobile_prefix(num):
  return num[0] == 7 or num[0] == 8 or num[0] == 9

# add phone number if unique
def add_phone_number(num):
    if not num in unique_codes and has_area_code(num):
      key = num.split(")")[0] + ")"
      unique_codes[key] = True
    elif not num in unique_codes and has_mobile_prefix:
      unique_codes[num[0:4]] = True

#Part B
#Keep track of Bangalore fixed lines
calls_from_Bangalore = 0
calls_to_Bangalore = 0

for call in calls:
  if call[sender][0:5] == "(080)":
    calls_from_Bangalore += 1
    if call[receiver][0:5] == "(080)":
      calls_to_Bangalore += 1
    add_phone_number(call[receiver])

print("The numbers called by people in Bangalore have codes: ")
print(*sorted(unique_codes.keys()), sep="\n")
print("{:.2%}".format(calls_to_Bangalore * 1.0/calls_from_Bangalore) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
