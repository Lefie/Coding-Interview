"""
Problem Statement:
Given a string with lowercase letters only, if you are allowed to replace no more 
than ‘k’ letters with any letter, find the length of the longest substring 
having the same letters after replacement.

"""

"""
Sliding Window Solution: O(N)
"""

def len_of_longest_substring(string,k):
    window_start = 0 #define where the window starts
    max_length = 0 #records our final answer
    max_repeated_letter_count = 0 #for each window, we keep track of the letter that is repeated the most times
    freq_map={} #a map that records the frequency of apperances of each letter
    for window_end in range(len(string)):
        cur_letter = string[window_end] # current letter we are working with 
        if cur_letter not in freq_map: # this block of code adds the letter in the frequency map 
            freq_map[cur_letter] = 0
        freq_map[cur_letter] += 1

        max_repeated_letter_count =  max(max_repeated_letter_count,freq_map[cur_letter]) #we update the varibale that stores the letter that appears most frequently in this particular window 

        
        #[window_end - window_start + 1] is the length of the substring aka the window we are currently at 
        #[max_repeated_letter_count] gives us the maximum repeated letter in a particular window 
        #[window_end - window_start + 1 - max_repeated_letter_count] gives us the number of remaining letters
        #if the number of remaining letters exceeds k, then we need to shrink the window 
        if (window_end - window_start + 1 - max_repeated_letter_count) > k:
            left_letter = string[window_start]
            freq_map[left_letter] -= 1 
            window_start += 1
        

        max_length = max (max_length, window_end - window_start + 1) #update the max length of the substring at each iteration
    return max_length 



string="aabccbb"
result1 = len_of_longest_substring(string ,2)
print(result1)


