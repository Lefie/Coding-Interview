"""
Problem Statement : Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, 
return the sum of the triplet with the smallest sum.
"""

import math

"""
Solution: O(N^2)
"""

def triple_sum_close(arr,target):
    arr.sort() #sort the array
    smallest_difference = math.inf #initiate this to the largest number

    for i in range(len(arr)-2): #we are searching in triplets. preventing it from going out of bound
        left_pt = i + 1  #initialize the pointers
        right_pt =len(arr) -1

        while (left_pt < right_pt):
            cur_sum = arr[i] + arr[left_pt] + arr[right_pt] #sum of values two pointers 
            target_dif = target - cur_sum #calculate the difference from the target 

            if target_dif == 0: #smallest sum we can get 
                return target
            
            if abs(target_dif) < abs(smallest_difference) or (abs(target_dif) == abs(smallest_difference) and target_dif > smallest_difference):
                smallest_difference = target_dif #update the smallest_difference 

            if target_dif > 0:
                left_pt += 1 # if the target difference is positive, it means we have a smaller cur_sum than target. increment the left pt
            else:
                right_pt -= 1 #otherwise, decrement the right pt 
    return target - smallest_difference



arr= [-2, 0, 1, 2]
target=2

result = triple_sum_close(arr,target)
print(result)