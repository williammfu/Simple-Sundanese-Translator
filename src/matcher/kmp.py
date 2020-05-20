"""
A simple implementation of
Knuth-Morris-Pratt (KMP) String
Matching algorithm
"""

def define_fail(pattern) :
    """
    Preprocess the pattern to find matches of
    prefixes of the pattern with the pattern itself.
    """
    
    # Defining variables
    length = len(pattern)
    fail = [0 for i in range(length)] # array of integer fail[]
    k = 1
    j = 0

    # Fail[0] is not defined
    fail[0] = 0

    # Initiate loop
    while k < length:
        if pattern[k] == pattern[j]: # found a matching suffix and prefix from 
                                     # pattern P[0..k-1]
            fail[k] = j + 1 # Sets the value of fail[k]
            k += 1
            j += 1
        else:
            if j > 0:
                # Previous prefix
                j = fail[j-1]
            else:
                # No matching prefix-suffix
                fail[k] = 0
                k += 1 # next index
    # k >= length

    return fail

def match_kmp_string(text, pattern):
    """
    Finds the first occurence of pattern
    inside of a text using KMP algorithm
    """

    #Defining Variables
    fail = define_fail(pattern)
    text_length = len(text)
    pattern_last_index = len(pattern) - 1
    i = 0 # For traversing text
    j = 0 # For traversing pattern, changes back and forth
    found = False # True, if pattern is found in text 

    if pattern_last_index + 1 > text_length:
        return -1   # Pattern is longer than text

    # Initiate loop
    while i < text_length and not found:

        if text[i] == pattern[j]: # Continue matching
            if j == pattern_last_index: # Pattern found
                found = True
            else : # Does an iteration
                i += 1
                j += 1
        
        else: # If pattern does not match, do a shift

            if j <= 0: # If the mismatch occured on the first index (index-0)
                       # does a shift to the right just for one step
                i += 1
            else:       # Finds the size of the next shift by
                        # the fail fucntion
                k = j-1
                j = fail[k]
        
    # i == text_length or found

    if found:
        # Index where pattern occured in text
        return i - pattern_last_index 
    
    return -1 # Pattern not found

def match(text, pattern):
    """
    Returns True if pattern
    is found within the text
    """
    return match_kmp_string(text, pattern) != -1
