"""
Question: Given an array of positive numbers and a positive number ‘k,’ 
find the maximum sum of any contiguous subarray of size ‘k’.
"""

"""
Brute Force Solution: O(N*K)
the idea here is to loop through all k-contiguous elements and record the highest sum
"""

from curses import window


def max_sub_brute(arr,k):

    max_sum = 0 #a variable to record the answer 
    for i in range(len(arr)-k+1): #loop through all the valid starting points
        cur_sum = 0 #sum of each window 
        for j in range(i,i+k): #from starting points to valid end points
            cur_sum += arr[j]
        max_sum = max(cur_sum,max_sum)

    
    return max_sum

"""
Optimized Solution: O(N)
- slide the window by one element forward at a time
- subtract the first element of the window
- add the new element
"""
def max_sub_opt(arr,k):
    max_sum = 0 #a variable to record the answer 
    window_sum = 0
    window_start = 0 # the index of the first element to be subtracted 

    for window_end in range(len(arr)): 
        window_sum += arr[window_end] #keep adding to the sum if we haven't hit K 
        if window_end >= k-1: 
            max_sum = max(max_sum,window_sum) #once we hit K, update max sum
            window_sum -= arr[window_start] #subtrat the first element of the window
            window_start += 1 #update the window by sliding it 
    return max_sum


arr=[2, 1, 5, 1, 3, 2]
result1=max_sub_brute(arr,3)
result2=max_sub_opt(arr,3)

print(result1)
print(result2)