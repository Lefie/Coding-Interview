"""
Problem Statement: 
Given an array containing 0s, 1s and 2s, sort the array in-place. 
You should treat numbers of the array as objects, 
hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, 
white and blue; and since our input array also consists of 
three different numbers that is why it is called Dutch National Flag problem.
"""

"""
Solution : O(N)
"""

def swap (arr,i,j): # a helper funciton that swaps values 
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 


def dutch_flag(arr):
    left = 0 #initiate the first pointer that points to the beginning 
    right = len(arr) - 1 #the second pointer initiated to the end 
    i = 0 # the ponter that helps us scan through the array 

    """
    Everything to the left of the left pointer is 0 
    everything to the right of the right pointer is 2
    everyrhing in between is 1
    if the scanner encounters and exceeds the right pointer, it is meaningless because we already know 
    they are all 2s.
    """

    while i <= right:
    #there are 3 cases to be considered 
        if arr[i] == 0:
            swap(arr,i,left) #we swap the value to the front and update both pointers 
            i += 1
            left += 1
        elif arr[i] == 1:
            i += 1 #we don't do anything. the left pointer doesn't change. update the scanner
        else: #if the value equal to 2
            swap(arr,i,right) # we swap the value to the end
            right -= 1 #we decrement the right pointer
            #the left pointer doesn't change
            #we dont update the scanner because the new scanner value will be evaluated again 


             
arr = [1, 0, 2, 1, 0]
dutch_flag(arr)
print(arr)

