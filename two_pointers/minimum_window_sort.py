"""
Problem Statement :
Given an array, find the length of the smallest 
subarray in it which when sorted will sort the whole array.

"""

import math 
"""
Solution: 0(N)

"""

def min_window_sort(arr):

    low = 0 #we define a pointer that points to the low end , moving from left to right 
    high = len(arr) - 1 #we define a pointer to the high end, moving from right to left 

    while (low < len(arr) - 1 and arr[low] <= arr[low + 1]): #checking to make sure that low is not going out of bound and that everything is in ascending order
        low += 1 #keep updating until we find the element that is out of order
    
    if low == len(arr) - 1: # in the case that the array is already sorted 
        return 0 
    
    while (high > 0 and arr[high] >= arr[high - 1]): #chekcing to make sure high does not go out of bound and everything is in ascending order 
        high -= 1 #keep updating until we find the element that is out of order

# now we look for the max and min of the subarray 
    sub_max = -math.inf
    sub_min = math.inf

    for k in range(low,high+1):
        sub_max = max(arr[k],sub_max)
        sub_min = min(arr[k],sub_min)

#now we compare the boundary elements to our new found min and max of the subarray to see if there is a need to extend the subarray 

    while low > 0 and arr[low - 1] > sub_min:
        low -= 1
    
    while high < len(arr)-1 and arr[high + 1] < sub_max :
        high += 1
    
    return high - low + 1



arr = [1, 2, 5, 3, 7, 10, 9, 12]
print(min_window_sort(arr))
