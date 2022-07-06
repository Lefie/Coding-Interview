"""
Problem Statement :
Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that 
each element appears only once. The relative order of the elements should be kept the same and you should not 
use any extra space so that that the solution have a space complexity of O(1).

Move all the unique elements at the beginning of the array and 
after moving return the length of the subarray that has no duplicate in it.
"""

"""
Solution O(N)
"""

def remove_duplicate(arr):
    next_non_duplicate = 1 #position of the next spot to store a non duplicate element 

    i = 0 #one pointer points at the beginning of the array. will iterate through the array and compare

    while (i < len(arr)):
        last_non_duplicate = arr[next_non_duplicate - 1] #all the elements up until this element (including this element) are unique or non-duplicates 
        cur_ele = arr[i] #extract the current element 

        if last_non_duplicate != cur_ele: #if the last unique element is not the same as current element
            arr[next_non_duplicate] = cur_ele #we store the unique element at next_non_duplicate
            next_non_duplicate += 1 #we update next_non_duplicate so that next time, when we find a special element, we store it here
        
        i += 1 # we always want to iterate through the array 
    
    return next_non_duplicate


arr=[2, 3, 3, 3, 6, 9, 9]
length = remove_duplicate(arr)
print(length)
