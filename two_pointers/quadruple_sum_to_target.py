"""
Given an array of unsorted numbers and a target number, 
find all unique quadruplets in it, whose sum is equal to the target number.
"""

"""
Solution : O(N^3)
"""

def find_quadrublets(arr,target):
    result = [] # a storage space for our result 
    arr.sort() #sort the array 

    for first in range(len(arr) - 3): #initiate our pointer to our first element (smallest) 
        if first > 0 and arr[first] == arr[first - 1]: #skip the duplicates!
            continue
        
        for second in range(first + 1, len(arr)-2): #initiate our pointer to our second element 
            if second > first + 1 and arr[second] == arr[second - 1]: #skip the duplicates 
                continue

            left = second + 1 #initiate the left pointer to point to our third element 
            right = len(arr) - 1 #initiate the right pointer to point to our fourth element which is the last number (biggest)

            while (left < right):
                cur_sum = arr[first] + arr[second] + arr[left] + arr[right] #calculate the sum of all four numbers 

                if cur_sum == target : #if sum is equal to target then we have found our answer
                    result.append([arr[first],arr[second],arr[left],arr[right]])
                    
                    #in this case, we update both pointers 
                    left += 1
                    right -= 1

                    #we also need to make sure we skip the duplicates 
                    while (left < right and arr[left] == arr[left - 1]):
                        left += 1
                    
                    while (left < right and arr[right] == arr[right + 1]):
                        right -= 1

                elif cur_sum < target : #if the current sum is too small, we will move the left pointer to the right to increase the value 
                    left += 1 
                else: #otherwise, if the current sum is too big, we will move the right pointer to the left to decrease the value 
                    right -= 1
    return result


"""
Testing :
"""
arr=[2, 0, -1, 1, -2, 2]
target = 2

result = find_quadrublets(arr,target)
print(result)
                







