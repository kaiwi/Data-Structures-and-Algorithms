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
#Make list of possible telemarkets
telemarketer_possibles = [] #O(1); initialize telemarketer list

#Must make outgoing calls
outgoing_calls = [caller for caller, recipient, datetime, duration in calls] #O(1); slice outgoing calls
incoming_calls = [recipient for caller,recipient, datetime, duration in calls] #O(1); slice incoming calls
outgoing_texts = [texter for texter, textee, datetime in texts] #O(1); slice outgoing texts
incoming_texts = [textee for texter, textee, datetime in texts] #O(1); slice incoming texts

#No receiving texts, No receiving calls, No sending texts
for caller in outgoing_calls: #O(n)
    if (caller not in incoming_calls) and (caller not in outgoing_texts) and (caller not in incoming_texts):
        telemarketer_possibles.append(caller)

#print result
print("These numbers could be telemarketers: ") #O(1)
for item in sorted(list(set(telemarketer_possibles))): #O(n log n) + O(n)
   print(item)
