"""
Quetion:
Given a string, 
find the length of the longest substring, 
which has all distinct characters.
"""

"""
Solution : O(N)
"""

def longest_substring_distinct_character(arr):
    window_start = 0 #initialize where our window will start
    max_length = 0 # a variable that helps us keep track of our answer
    index_map ={} #a hash map that will record the index of the character last appeared 

    for window_end in range(len(arr)):
        cur_item =  arr[window_end] #grab the item that is currently being worked on
        if cur_item in index_map : #if we find a duplicare, then we update the start pointer to the index of the original poistion + 1 
            window_start =  max(window_start,index_map[cur_item]+ 1) #making sure that our start pointer doesn't go backwards 
        
        index_map[cur_item] = window_end #either way,we either add new item's index to dictionary or update the current item's index 
        max_length = max(max_length , window_end - window_start + 1) #we calculate the max length at each iteration
    return max_length 

arr= ['a','b','c','b','a','f','g']

result=longest_substring_distinct_character(arr)
print(result)
        





