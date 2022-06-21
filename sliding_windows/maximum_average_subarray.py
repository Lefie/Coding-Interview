"""
Question: Given an array, find the average of all  subarrays of ‘K’ contiguous 
elements in it.
"""

"""
Brute Force solution: #O(N*K)
- loop through every k contiguous element and calculate all of their avergaes
"""

def max_ave_subarr_brute(arr,k):
    if k > len(arr): #if k is bigger than the length of the array, then it doesn't exist
        return None
    result = [] #an auxiliary space to store the result 
    
    for i in range(len(arr)-k+1): # loop through all the valid starting points
        window_sum = 0  #initilize the window sum from a particular starting point to 0
        for j in range(i,i+k): #from the starting point to end point, add all the values in between
            window_sum += arr[j] 
        ave = window_sum/k #calculate the average 
        result.append(ave) #append the result to the list

    return result



    
    
"""
sliding window solution : O(N)
- slide the window by one element forward at a time
- subtract the first element of the window
- add the new element 
"""

def max_ave_subarr_opt(arr,k):
    if k > len(arr): #if k is bigger than the length of the array, then it doesn't exist
        return None
    result = [] #an auxiliary space to store the result 
    window_sum = 0.0 #sum of every window
    window_start = 0 #a variable to keep track of the index of the element that we subtract

    for window_end in range(len(arr)):
        window_sum += arr[window_end] #if we have not hit k contiguous element, we just keep adding to the sum

        if window_end >= k-1: 
           ave = window_sum / k #calculate the average 
           result.append(ave)
           window_sum -= arr[window_start] #subtract the first element of the window
           window_start += 1 #update the index of the first element of the window
    return result


arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
result1 = max_ave_subarr_brute(arr ,5)
result2 = max_ave_subarr_opt(arr,5)

print(result1)
print(result2)




