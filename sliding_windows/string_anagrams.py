"""
Question: Given a string and a pattern, 
find all anagrams of the pattern in the given string.

Write a function to return a list of starting indices of 
the anagrams of the pattern in the given string.
"""

"""
Solution using sliding window O(N)
"""

def find_anagrams(str1, pattern):
    window_start = 0 #we define where the window would start 
    matched = 0 #a variable which keeps track of the letters that match the pattern
    char_frequency = {} # a dictionary which records the frequencies of each letter in the pattern
    result = [] #will record the indices of the start of a permutation and be returned as the result
    #this block of code will record the frequencies of letter in the pattern 
    for char in pattern :
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
    
    for window_end in range(len(str1)): #now we loop through the string sequence to check each letter
        cur_char = str1[window_end] #grab the current letter in the string we are working with

        #if the character in the string appears in the pattern [which we recorded in a dictionary], then decrement the frequency of the character
        if cur_char in char_frequency:
            char_frequency[cur_char] -= 1
            if char_frequency[cur_char] == 0: #if the character's frequency in the dictionary becomes 0, then it means that we have found a match 
                matched += 1
        
        if matched == len(char_frequency): #if the number of characters that match the pattern is the same as the pattern's length , then we have found all that match 
            result.append(window_start) #we will add the start indice to the result
        
        if window_end >= len(pattern) - 1:  #if the window size is bigger than or equal to the pattern's length, we need to shrink the window 
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency: #if the character that is going out is in the dictionary 
                if char_frequency[left_char] == 0: #if the character is in the match, we will remove it from the match
                    matched -= 1
                
                char_frequency[left_char] += 1 #we will give the character back to the dictionary 
        
    return result

"""
Test:
"""
string = "oidbcaf"
pattern = "ac"

print(find_anagrams(string,pattern))
