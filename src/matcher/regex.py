"""
A simple implementation
of string matching using
Regular Expression
"""

# Imports Python's RE module
import re


def match(text, pattern):
    """
    Returns true if the given pattern
    exists inside the text
    """
    if len(text) < len(pattern):
        return False
    
    expression = r"{}".format(pattern)
    return len(re.findall(expression, text)) > 0
 