"""
Question:
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.
"""

"""
Solution: O(N)
used sliding window 
"""

def longest_subarray_with_ones(arr,k):
    window_start = 0 #initiate where the window would start 
    max_length = 0 #will return the answer we record 
    max_repeated_ones = 0 #will record the number of 1s in each specific window 

    for window_end in range(len(arr)):
        cur_ele = arr[window_end] 
        if cur_ele == 1: #we will keep track of how many 1s we have in each window
            max_repeated_ones += 1
        
        len_of_window = window_end - window_start + 1 #the size of the current window at the moment 
        num_of_zeroes = len_of_window - max_repeated_ones #we get the number of 0s in a particular window after subtracting the 1s

        if num_of_zeroes > k: #if the 0s exceed k, then according to the requirement, we cannot replace them all, so we must shrink the window 
            left_ele = arr[window_start] #if the window start element is 1, then we decrement the frequency 
            if left_ele == 1:
                max_repeated_ones -= 1
            window_start += 1 #we move the start pointer 
        
        max_length = max(max_length, window_end - window_start + 1)
    return max_length






arr=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
K=2

print(longest_subarray_with_ones(arr,K))