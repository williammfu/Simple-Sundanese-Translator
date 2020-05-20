"""
File: translator.py
A simple Bahasa Indonesia - Basa Sunda
translator application using
- KMP Algorithm
- BM Algorithm
- Regular Expression (RE)
"""
import time
import sys
import re
from translate import dictionary
sys.path.append("../")

from matcher import bm, kmp, regex

class Translator:

    def __init__(self, dictionary):
        """
        Constructing an instance of Translator
        """
        self.dictionary = dictionary
        self.keywords = list(dictionary.keys())
        self.phrases_dict = []
        self.text = ""
        self.stopwords = []
        for keyword in self.keywords:
            if " " in keyword:
                self.phrases_dict.append(keyword)
    
    def generate_split(self, matcher):
        """
        Splits a given text into words 
        or phrases
        """

        pattern = r""
        PUNCT = r"[\?\!\.\,\'\"\&\(\)\[\]\`]"
        
        for phrase in self.phrases_dict:
            if matches(self.text, phrase, matcher):
                pattern += r"{}|".format(phrase)
        
        pattern += r"\w+|{}".format(PUNCT)

        return re.findall(pattern, self.text.lower())

    def set_text(self, text):
        """ Sets text to be translated """
        self.text = text

    def set_stopwords(self, stopwords):
        """ Sets the given stopwords """
        self.stopwords = stopwords

    def translate_text(self, matcher):
        """
        Translates a given text
        with the dictionary given
        """ 

        translation = ""
        words = self.generate_split(matcher)
        
        for word in words:
            
            match = False
            key = ""
            tr_word = ""

            if is_punct(word):
                match = True
                tr_word = word
            else:
                for stopword in self.stopwords:
                    if matches(stopword, word, matcher):
                        match = True
                        break
                
            if not match:

                i = 0
                while i < len(self.keywords) and not match:
                    if len(word) == len(self.keywords[i]) and matches(self.keywords[i], word, matcher):
                        key = word
                        match = True
                    i += 1
                # found match OR out of bounds
        
                if match:
                    if isinstance(self.dictionary[key], list):
                        tr_word = self.dictionary[key][0]
                    else:
                        tr_word = self.dictionary[key]
                    
                    if subject_match(tr_word, matcher) and len(words) > 0 and " teh" not in translation:
                        tr_word += " teh"
                    elif question_match(tr_word, matcher) and translation != "" " teh" not in translation:
                        tr_word = "teh " + tr_word
                
                else:
                    tr_word = word

            translation += tr_word + " "
            
        return translation
        


def matches(text, pattern, matcher, exact=False):
    """
    Returns True if pattern is
    found in the given text
    
    Parameters:
    text (str): text string
    pattern (str): pattern string
    matcher (kmp): matching algorithm option

    Returns:
    bool : found boolean
    """
    # For an exact match, return false if
    # strings have different length
    if exact and len(text) != len(pattern):
        return False

    if matcher == "kmp":
        return kmp.match(text, pattern)
    elif matcher == "bm":
        return bm.match(text, pattern)
    else: # assume "re"
        return regex.match(text, pattern)

def subject_match(word, matcher):
    """
    Returns true if the given word 
    matches a subject pronoun (in Basa Sunda)
    """
    return (matches("abdi", word, matcher, exact=True) or matches("urang", word, matcher, exact=True) 
    or matches("anjeun", word, matcher, exact=True) or matches("manehna", word, matcher, exact=True))

def question_match(word, matcher):
    """
    Returns true if the given word 
    matches a question identifier (in Basa Sunda)
    """
    return (matches("saha", word, matcher, exact=True) or matches("naon", word, matcher, exact=True) 
    or matches("kawit", word, matcher, exact=True) or matches("iraha", word, matcher, exact=True)
    or matches("sabaraha", word, matcher, exact=True))

def is_punct(text):
    """
    Returns true if the given word 
    matches a punctuation (in Basa Sunda)
    """
    return text in [",",".","/","!","?","&"]