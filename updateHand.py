# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:59:12 2020

@author: anwar
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    
    Update the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    
    Has no side effects: does not modify hand.
    
    word: string
    hand: dictionary(string -> int)
    returns: dictionary (string -> int)
    
    """
    
    output = hand.copy()
    for letter in word:
        if letter in output.keys():
            output[letter] -= 1
    return output