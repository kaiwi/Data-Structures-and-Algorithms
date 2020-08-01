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
#Need to find out how long each phone number spent on the phone then max.
#get unique numbers
#check calls[0] against unique and add calls[3] to unique[n].

duration_log = [] # list of tuples of [number, duration]


for item in calls: #O(n)
    item[3] = float(item[3]) #O(1); convert call duration to float
    for number in item[:2]: #O(1)x2
        if not [a for a in duration_log if a[0] == number]: #O(1): list comprehension; check if number is unique
            duration_log.append([number,item[3]]) #O(1)
        else:
            #not unique; add to duration
            #find number and add duration to item[3]
            [a for a in duration_log if a[0] == number][0][1] += item[3] #O(1); list comprehension to add time to non-unique numbers

print(list(map(max,zip(*duration_log)))[0],"spent the longest time,",list(map(max,zip(*duration_log)))[1],"seconds, on the phone during September 2016.") #O(n) -> zip
