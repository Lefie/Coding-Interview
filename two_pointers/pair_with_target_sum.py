"""
Problem Statement:
Given an array of sorted numbers and a target sum, find a pair in the array whose 
sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) 
such that they add up to the given target.

"""




# Solution : O(N)

def find_pair(arr,target):
    
    #we define two pointers: pt1 pointing at the beginning and pt2 pointing at the end
    pt1 = 0 
    pt2 = len(arr) - 1
    
    
    #while the two pointers have not crossed each other
    while pt1 < pt2:
        cur_sum = arr[pt1] + arr[pt2] #we compare the sum of the current two elements to the target value 
        if cur_sum == target: #we return the two indices if we have found the right pair 
            answer_list = [pt1,pt2]
            return answer_list
        
        if cur_sum > target: # otherwise if the sum is larger than the target, we decrement pt2 
            pt2 -= 1
        else:
            pt1 += 1 #if the sum is smaller, then we increment pt1
        
    return None #return None if no such pair is found


# Here is an alternative O(N) solution where a hash map is utilized 
def alternative(arr,target):
    hash_table={} # a dictionary to record the element and its inddex

    for i in range(len(arr)): #record all elements and their indices in the array
        hash_table[arr[i]] = i
    
    for i in range(len(arr)): 
        complement = target - arr[i] #find complememt to the target
        if complement in hash_table: #if the complement is found in the hash map, we have found the pair 
            answer1 = i
            answer2 = hash_table[complement]
            answer=[answer1,answer2]
            return answer
    
    return None #if nothing is found ,return None

"""
Testing
"""

arr=[2,5,9,11]
target = 20

result = find_pair(arr,target)
result2 = alternative(arr,target)

print(result)
print(result2)


        
