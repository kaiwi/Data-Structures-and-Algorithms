Your paragraph should not be a detailed walkthrough of the code you provided, 
but provide your reasoning behind decisions made in the code. For example, why 
did you use that data structure? You also need to explain the efficiency 
(time and space) of your solution.

I used a helper function to make a recursive call on the current working directory path to traverse all sub-folders 
and files.

Time complexity\
return_find_files(): O(n) - len(os.listdir())    

Space complexity\
return_find_files(): O(n) - Space need grows linearly with number of file paths.\ 