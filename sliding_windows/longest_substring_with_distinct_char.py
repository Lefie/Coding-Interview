"""
Question : Given a string, find the length of the longest substring in it with no more than K distinct characters.
You can assume that K is less than or equal to the length of the given string.
"""

"""
Solution : Sliding window + hash map O(N)
"""

def longest_substring_with_k_distinct(string,k):
    window_start = 0 #initialize a start pointer
    max_length = 0 #a variable which keeps track of the answer
    char_frequency = {} # a dictionary/hash map which keeps track of the frequency of every character in the string 

    # store the frequency of the characters in the string in a dictionary :
    for window_end in range(len(string)): 
        cur_char = string[window_end] #the current character we are working on 
        if cur_char not in char_frequency: #if the current character is not in our dictionary, we initialize it to 0
            char_frequency[cur_char] = 0 
        char_frequency[cur_char] += 1 #we also calculate the frequency if we see the character appear 
    
    #while the number of distinct values exceeds k , we need to shrink the window  
        while len(char_frequency) > k: 
            start_char = string[window_start] #we grab the element at the very beginning and remove it 
            char_frequency[start_char] -= 1 #we remove it by decreasing the frequency 
            if char_frequency[start_char] == 0: # if the frequency of a character is 0, then we delete it from the map altogether 
                del char_frequency[start_char]
            window_start += 1 #we update the start pointer 
    
        max_length = max(max_length, window_end - window_start + 1)
    return max_length 

string="araaci"
K=2

print(longest_substring_with_k_distinct(string,K))
        







