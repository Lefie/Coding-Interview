"""
Question: 
Given an array of positive numbers and a positive number ‘S,’ 
find the length of the smallest contiguous subarray whose sum is 
greater than or equal to ‘S’. Return 0 if no such subarray exists.

"""

"""
Brute Force Solution: O(N*K)
the idea here is to check every possible subarray and find the solution
"""

def min_size_sub_brute(arr,s):
    min_length=float('inf') #initilize the min length as positive infinity 
    for i in range(len(arr)): #loop through every element in the array 
        cur_sum = 0 #reset current sum every time we move to a new element 
        for j in range(i,len(arr)): #the second pointer goes from i to the end of the array
            cur_sum += arr[j] #calculate the current sum 
            if (cur_sum >= s): #check if current sum is bigger than or equal to the given S
                min_length = min(min_length, j-i+1) #as soon as we find it, we update the min_length if possible
                break #we break out of the inner loop and move forward with the outer loop
    return min_length #return value 


"""
Optimized Solution: O(N)
the idea here is to reasonably add and shrink the window as we slide

"""
def min_size_sub_opt(arr,s):
    
    window_start = 0 #initilize a window start pointer [left pointer]
    min_length = float('inf') #initialize the min_length to positive infinity 
    cur_sum = 0 #a variable to keep track of the sum of values 

    for window_end in range(len(arr)): 
        cur_sum += arr[window_end] # keep adding values to the sum by sliding the end pointer if we haven't hit the target S value yet 
        while cur_sum >= s: #once we hit the s value, use a while loop to trap the end pointer. compare cur_sum to the target S value 
            min_length = min(min_length,window_end - window_start + 1) #update the minimum length 
            cur_sum -= arr[window_start] #get rid of the start pointer value 
            window_start += 1 #shrink the window by moving the start pointer to the right 

    if min_length == float('inf'): #if min_length's initial value wasn't changed at all, then it means that we didn't find anything that would satisfy the S target 
        return 0 #in this case, return 0 

    return min_length

arr = [2, 1, 5, 2, 3, 2]
target = 7

result1= min_size_sub_opt(arr,7)
print(result1)

result2= min_size_sub_brute(arr,7)
print(result2)





