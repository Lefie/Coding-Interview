"""
Comparing Strings containing Backspaces
"""

"""
Solution 1: Stack based Approach 0(M+N)
"""

def backspace_stack(s1,s2):
    # we process both strings by applying backspaces to both
    str1 = process_string(s1) 
    str2 = process_string(s2)

    if str1 == str2: #simply compare the strings from here
        return True
    else:
        return False

def process_string(s):
    processed_string = [] #we initiate an empty stack 
    for i in s : #iterating through the string 

        if i == "#": #if we encounter a #, we immediately pop the last item (item before #) off the stack 
            processed_string.pop()
        else:
            processed_string.append(i) #otherwise, we keep adding non-# values
    
    new_string = "".join(processed_string) #join them into a string 
    return new_string


"""
Solution2 : 0(M+N)

"""

def get_next_valid_char_index(str1,index): # a helper function that finds the next valid character index to start comparing strings
    backspace_count = 0 #use a counter to track how many backspaces and how many valid letters to skip 
    while index >= 0: 
        if str1[index] == "#": # if we encounter the # symbol, we keep the count so we know how many letters to skip 
            backspace_count += 1
        elif backspace_count > 0: #if the count is bigger than 0, then we reduce the count 
            backspace_count -= 1
        else: #in other scenarios, we break out of the loop becasue we have found a fresh start to compare string
            break 
        index -= 1 #we move backwards each time 

    return index 


def string_compare(str1,str2):
    #initiate the two pointers at the end of both strings 
    indx1 = len(str1) - 1
    indx2 = len(str2) - 1

    while (indx1 >= 0 or indx2 >= 0): 
        i1 = get_next_valid_char_index(str1,indx1) #find the next valid character index for string 1
        i2 = get_next_valid_char_index(str2,indx2) # find the next valid character index for string 2

        if i1 < 0 and i2 < 0: #we have reached the end of both strings
            return True 
        
        if i1 < 0 or i2 < 0: # if one string is at the end and the other doesn't, then the two strings aren't the same
            return False
        
        if str1[i1] != str2[i2]: #if the characters are different , then the strings aren't the same
            return False
        
        indx1 = i1 - 1 
        indx2 = i2 - 1
    return True 


    





"""
Testing
"""
string1 ="xx#yzz##"
string2 ="xyz##"

print(backspace_stack(string1,string2))
print(string_compare(string1,string2))















    







