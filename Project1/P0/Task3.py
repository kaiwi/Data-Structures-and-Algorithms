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

#PART A
bangalore_calls = [(caller,recipient) for caller,recipient,datetime,duration in calls if caller[:5] == "(080)"] #O(1); slice Bangalore calls
bangalore_callers = [caller for caller, recipient in bangalore_calls] #O(1); slice callers
bangalore_recipients = [recipient for caller, recipient in bangalore_calls] #O(1); slice recipients

#create a list fixed lines, mobile, and telemarketers
#prefix filtering
bangalore_recipients_unique = list(set(bangalore_recipients)) #O(1); create unique recipient list

#slice by prefix types
bangalore_recipient_mobile_code = list(set([number[:4] for number in bangalore_recipients_unique if number[0] in ('7','8','9')])) #O(1); slice mobile
bangalore_recipient_telemarketer_code = list(set([number for number in bangalore_recipients_unique if number[:2] == '140'])) #O(1); slice telemarketers
bangalore_recipient_fixed_code = list(set([number[1:number.index(')')] for number in bangalore_recipients_unique if number[0] == '('])); #O(n); slice fixed

print("The numbers called by people in Bangalore have codes:") #O(1)
bangalore_codes = sorted(bangalore_recipient_fixed_code+bangalore_recipient_mobile_code+bangalore_recipient_telemarketer_code) #O(1)
for item in bangalore_codes: #O(n log n) + O(n)
    print(item)
#PART B
bangalore_local_calls = [number for number in bangalore_recipients if number[:5] == '(080)'] #O(1); slice bangalore_recipients for local numbers only

print(round(100*len(bangalore_local_calls)/len(bangalore_recipients),2),"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.") #O(1)
