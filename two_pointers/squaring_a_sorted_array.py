"""
Problem Statement : Given a sorted array, create a new array containing squares of all the numbers of 
the input array in the sorted order.

"""

"""
Solution : O(N)
"""
def square_array(arr):
    n = len(arr) #length of the array
    result = [0 for x in range(n)]
    left = 0 #initiate left pointer to be 0
    right = n-1 #initiate right pointer to be the position of the last element 
    highest_value_index = n-1 # we are storing elements from the biggest to smallest, so we are storing it backwards 

    while left <= right :
        #getting the squares of the two elements from both ends
        left_val = arr[left] * arr[left] 
        right_val = arr[right] * arr[right]

        if left_val > right_val: #ifthe left value is bigger than the right value , we record left
            result[highest_value_index] = left_val
            left += 1 #update the left pointer 
        else:
            result[highest_value_index] = right_val  #vice versa
            right -= 1
        highest_value_index -= 1 #since we are storing answers backwards, we decrement the index 

    return result 

"""
Testing
"""
arr= [-2, -1, 0, 2, 3]
result = square_array(arr)
print(result)





