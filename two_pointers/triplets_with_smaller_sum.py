"""
Triplets with smaller sum :
Given an array arr of unsorted numbers and a target sum, count all triplets 
in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three
 different indices. Write a function to return the count of such triplets.

"""

"""
Solution: O(N^2)
"""

def triplets_smaller(arr,target):
    count = 0 # count the number of valid triplets 
    arr.sort() #sorting an array

    for i in range(len(arr)-2): # i will be our first index
        left = i + 1 #initiate the pointer for the second index
        right = len(arr) - 1 #initiate the pointer for the third index at the end of the array 
        while left < right : #when the two pointers don't cross each other 
            cur_sum = arr[i] + arr[left] + arr[right] #we calculate the sum of the current 3 values at the 3 indices
            if cur_sum < target: #if sum is smaller than target, that means the sum of any value between left and right plus the arr[i] is smaller than target 
                count += right - left 
                left += 1 #update the pointer for the second index
            else:
                right -= 1 #update the pointer for the third index 
    
    return count # return the count 


nums = [-1, 4, 2, 1, 3]
target = 5

result = triplets_smaller(nums,target)
print(result)