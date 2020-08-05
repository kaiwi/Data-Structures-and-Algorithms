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

#dissect each tuple into phone number and duration
#append list

#duration_log = list(map(lambda x: (x[0],float(x[3])),calls)) + list(map(lambda x: (x[1],float(x[3])),calls)) #O(2n)

duration_log = {} #O(1)
for caller, recipient, datetime, duration in calls: #O(6n)
    duration_sum = duration_log.get(caller,[])
    duration_sum.append(float(duration))
    duration_log[caller] = duration_sum
    duration_sum = duration_log.get(recipient, [])
    duration_sum.append(float(duration))
    duration_log[recipient] = duration_sum

temp = [] #O(1)
for item in duration_log.items(): #O(n)
    temp.append([item[0],sum([time for time in item[1]])]) #O(m) where m <= n/2

print(max(temp,key = lambda x: x[1])[0],"spent the longest time,",max(temp,key = lambda x: x[1])[1],"seconds, on the phone during September 2016.") #O(2n)


