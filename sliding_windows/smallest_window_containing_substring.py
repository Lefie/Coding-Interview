"""
Problem Statement:
Given a string and a pattern, find the smallest substring in the given 
string which has all the character occurrences of the given pattern.
"""

"""
Solution : O(N)
"""

def find_substring(str1, pattern):
    window_start = 0 #define where the window will start
    matched = 0 #a variable which keeps track of the characters which are matched 
    min_len = len(str1) + 1 #a variable that keeps track of the minimum length of the valid substring 
    substring_start = 0 # a variable that keeps track of at which index our result substring starts 
    char_freq={} # a hash map which stores the frequencies of characters in the pattern

    # we add the frequencies from the pattern into the hash map 
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    
    for window_end in range(len(str1)): #we iterate through the string sequence 
        cur_char = str1[window_end]  #current character we are working with 
        if cur_char in char_freq: 
            char_freq[cur_char] -= 1 #we decrement the frequency of the character if it appears in the string 
            if char_freq[cur_char] >= 0: #if after decrementing,the frequency is bigger than or equal to 0, then we have found a match 
                matched += 1 
        
        while matched == len(pattern): #when matched is equal to the length of the pattern, it means that every letter in the pattern has appeared in the string
            if min_len > window_end - window_start + 1: #find a smaller substring that satisfied the conditions if we can 
                min_len = window_end - window_start + 1
                substring_start = window_start #update where the substring start of the shortest valid substring is at 

            left_char = str1[window_start] #we will try to shrink the window whenever we have matched all the characters
            window_start += 1
            if left_char in char_freq: #we remove a match when the the frequency of the character we are trying to remove is 0 
                if char_freq[left_char] == 0:
                    matched -= 1 
                char_freq[left_char] += 1 #put it back in the dictionary 
        
    if min_len > len(str1): #return an empty string if we can't find any 
            return ""
    return str1[substring_start:substring_start + min_len] #other wise, return the sub string that we found 

                
"""
Test
"""

string="aabdec"
pattern="abc"

print(find_substring(string,pattern))