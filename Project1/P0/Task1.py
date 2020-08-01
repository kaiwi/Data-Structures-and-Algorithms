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
records = texts + calls #merge lists to get total recordset #O(1)
unique_numbers = set()  #initialize unique numbers list #O(1)
for item in records: #O(n)
    unique_numbers.add(item[0])
    unique_numbers.add(item[1])

print("There are",len(unique_numbers),"different telephone numbers in the records.") #O(1)
