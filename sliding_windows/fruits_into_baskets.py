"""
Problem Statement
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.
"""

"""
solution : O(N)
this problem can be transformed to longest substring with 2 distinct characters 
"""

def fruits_in_basket(arr):
    window_start = 0 #initialize where the window starts
    max_num = 0 #a variable that will record the answer for us 
    char_freq={} # a dictionary to keep track of the frequencies of appearances of characters 

    for window_end in range(len(arr)): #this part of code loops through the array and record frequencies of character
        cur_item = arr[window_end] 
        if cur_item not in char_freq: 
            char_freq[cur_item] = 0
        char_freq[cur_item] += 1

        while len(char_freq) > 2: # we keep going until our dictionary records 3 types of different characters. 
            item_start = arr[window_start] #in this case, we will be shrinking the window start 
            char_freq[item_start] -= 1 #we shrink by decreasing the frequency of the first fruit tree
            if char_freq[item_start] == 0: #if we have no more fruit tree, we remove the tree altigether from the dictionary 
                del char_freq[item_start]
            window_start += 1 #we update the new window start 
        
        max_num =  max (max_num , window_end - window_start + 1) #at each turn, we keep track of the maximum number of fruits we get from the 2 fruit trees 
    
    return max_num #we return the answer
        



Fruit=['A', 'B', 'C', 'A', 'C']
result1 = fruits_in_basket(Fruit)
print(result1)
