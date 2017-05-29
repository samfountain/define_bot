"""
Quick define test
"""

from PyDictionary import PyDictionary

def define(word: str):
    """
    define word and return meanings
    """
    dictionary = PyDictionary()
    meanings = dictionary.meaning(word)
    return meanings

print(define('test'))
