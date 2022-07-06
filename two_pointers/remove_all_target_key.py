"""
 Given an unsorted array of numbers and a target ‘key’, remove all 
 instances of ‘key’ in-place and return the new length of the array.
"""

"""
Solution : O(N)
"""

def remove_all_keys(arr,key):
    next_position = 0 #element at the next position to be changes
    i = 0 

    while i < len(arr):
        if arr[i] != key:  #if the element does not equal to key , we put this element at the next available position
            arr[next_position] = arr[i]
            next_position += 1 #update the next available position
        i += 1 #update the other pointer
    
    return next_position


"""
Testing 
"""

arr =[2,3,3,3,6,9,9]
key =3

length = remove_all_keys(arr,key)
print(length)