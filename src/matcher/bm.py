"""
A simple implementation
of Boyer-Moore String
Matching algorithm
"""

def compute_last_ocurrence(pattern):
    """
    Preprocesses the pattern
    and the alphabets occured in
    the pattern 
    """

    # Defining Variables

    # last_occurence equals to -1 
    # if the alphabet did not occur in the pattern
    last_occurence = [-1 for i in range(10000)]
    pattern_last_index = len(pattern) - 1
    
    # Mapping the pattern
    for i in range(pattern_last_index, -1, -1):
        bit_value = ord(pattern[i])
        if last_occurence[bit_value] == -1:
            last_occurence[bit_value] = i
    
    return last_occurence


def match_bm_string(text, pattern):
    """
    Finds the first occurence of pattern
    inside of a text using BM algorithm
    """

    # Defining Variables
    last_occurence = compute_last_ocurrence(pattern)
    pattern_last_index = len(pattern) - 1
    text_length = len(text)
    found = False
    i = pattern_last_index # For traversing text
    j = pattern_last_index # For traversing pattern, changes back and forth
                           # Looking glass technique - starts from the last index


    if pattern_last_index > text_length - 1:
        return -1   # Pattern is longer than text

    # Initiate loop
    while not found and i <= text_length - 1:
        
        if pattern[j] == text[i]: # Continue matching
            
            if j == 0:
                found = True # Pattern found
            else:
                # Implements looking glass technique
                # Does an iteration backwards
                i -= 1
                j -= 1
        
        else: # If not match, do a shift

            if i > text_length -  1:
                break
            # Determines the next text index i 
            # to start from based on the Character Jump technique
            
            last_occur = last_occurence[ord(text[i])] # Finding character's last occurence in the pattern
            i += pattern_last_index + 1

            if last_occur == -1: 
                # Case 3
                # When the given character in text 
                # did not occur inside the pattern
                i += 0
            elif last_occur + 1 > j: 
                # Case 2
                # When the given character exists in the pattern
                # but a right shift to the last occured character is not possible
                i -= j
            else: 
                # Case 1
                # When a given chracter exixts in the pattern
                # and a right shift to its last occurence is possible
                i -= (last_occur + 1) # Aligns text to the last occurence

            j = pattern_last_index

    # found or j > text_length

    if found:
        return i # returns the string's starting index
    
    return -1 # If not found, returns -1
            
def match(text, pattern):
    """
    Returns True if pattern
    is found within the text
    """
    return match_bm_string(text, pattern) != -1