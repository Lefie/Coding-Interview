"""
Given an array of unsorted numbers, 
find all unique triplets in it that add up to zero.
"""

"""
Solution : O(N log N) + O(N^2) --> O(N^2)
 
"""


def find_triplets(arr):
    arr.sort()
    result=[]

    for i in range(len(arr)): #scanning the array
        if i>0 and arr[i] == arr[i-1]: #starting from the second index, if any element is deteceted as a duplicate, we ignore it
            continue
        find_pairs(arr,-arr[i],i+1,result) #run the function below to find triplet pairs. 
    
    return result

def find_pairs(arr,target_sum, left_ptr,result):
    right_ptr = len(arr) - 1 #we initiate right pointer at the end of the array
    
    while left_ptr< right_ptr:  
        cur_sum = arr[left_ptr] + arr[right_ptr] #we calculate the current sum of values pointed at by two pointers
        if cur_sum == target_sum: #we have found a triplet 
            result.append([-target_sum,arr[left_ptr],arr[right_ptr]]) #append the triplet to the result list 
            left_ptr += 1 #update the pointers 
            right_ptr -= 1

            while left_ptr < right_ptr and arr[left_ptr] == arr[left_ptr-1]: #a duplicate has been foun
                left_ptr += 1
            
            while left_ptr < right_ptr and arr[right_ptr] == arr[right_ptr+1]: #a duplicate has been found!
                right_ptr -= 1

        elif cur_sum >= target_sum: #if current sum is bigger than target, we need a smaller sum
            right_ptr -= 1
        else: #if current sum is smaller than target, we need a bigger sum
            left_ptr += 1 



arr =[-3, 0, 1, 2, -1, 1, -2]
print(find_triplets(arr))









