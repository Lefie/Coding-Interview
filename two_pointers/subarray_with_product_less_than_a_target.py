from collections import deque


"""
Problem Statement:
Given an array with positive numbers and a positive target number, 
find all of its contiguous subarrays whose product is less than the target number.
"""

"""
Solution: O(N^3) worst case
Technique : sliding window + two pointers 
"""
def numSubarrayProductLessThanK(nums, k):
    result =[] # a storage space to store the answers
    product = 1 #initiate the product to 1. it will store the accumulated product 
    window_start = 0 #initiate the start of the window to be 0

    for window_end in range(len(nums)):
        product *= nums[window_end] #we accumulate the product element by element 
        while product >= k: #if the product is bigger than the target 
            product /= nums[window_start] #we remove the element at the beginning of the window 
            window_start += 1 #we update the pointer that points to the window start

        temp_list = deque() #we store the valid subarray in here
        for i in range(window_end, window_start-1, -1):
            temp_list.appendleft(nums[i])
            result.append(list(temp_list))

    return result
       
"""
Testing
"""

arr=[2, 5, 3, 10]
target=30 
result = numSubarrayProductLessThanK(arr,target)
print(result)



