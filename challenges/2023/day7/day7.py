"""Advent of Code 2023, Day: 7
Author: David Eyrich
Link: https://adventofcode.com/2023/day/7"""

import os
import sys

scripts_path = os.getcwd()
scripts_path_split = scripts_path.split('/')
scripts_path_join = '/'.join(scripts_path_split[:-2])
sys.path.append(f"{scripts_path_join}/aoc_mod/src")

from sess_id_u_agent import USER_AGENT, SESSION_ID
from submit_ans import submit

def parseInput(filename):
    # read in from a file
    with open(filename, 'r') as f:
        input = f.read()
    
    # parse through input here
    parsedInput = input.split('\n')
    
    parsedInput = [line.split() for line in parsedInput]
    
    parsedInput = [(hand, int(stren)) for hand, stren in parsedInput]
    
    return parsedInput

"""

Rules of Camel Poker:

Each hand is scored with the following types, in descending 
order of precedence.

    > Five of a kind, where all five cards have the same label: AAAAA
    > Four of a kind, where four cards have the same label and one card 
        has a different label: AA8AA
    > Full house, where three cards have the same label, and the 
        remaining two cards share a different label: 23332
    > Three of a kind, where three cards have the same label, and the
        remaining two cards are each different from any other card in
        the hand: TTT98
    > Two pair, where two cards share one label, two other cards share 
        a secor nd label, and the remaining card has a third label: 23432
    > One pair, where two cards share one label, and the other three 
        cards have a different label from the pair and each other: A23A4
    > High card, where all cards' labels are distinct: 23456

For hands of the same types, go through each card, in order, and determine
which card is higher.

"""

AAAAA = 1 # five of a kind
AAAA2 = 2 # four of a kind
AAABB = 2 # full house
AAA45 = 3 # three of a kind
AABBC = 3 # two pair
AABCD = 4 # one pair
ABCDE = 5 # high card

global_vals = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "T": 10,
        "J": 11, "Q": 12, "K": 13, "A": 14}

global_vals_2 = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "T": 10,
        "J": 0, "Q": 12, "K": 13, "A": 14}

# returns 1 if val1 is greater and 0 if not
def is_val_greater(val1, val2):
    if global_vals[str(val1)] > global_vals[str(val2)]:
        return 1
    elif global_vals[str(val1)] < global_vals[str(val2)]:
        return 0
    return -1

# returns 1 if hand1 is greater and 0 if not
def winning_hand(hand1, hand2):
    cards_1 = dict()
    cards_2 = dict()
    
    for card in hand1:
        if card in cards_1:
            cards_1[card] = 1 + cards_1[card]
        else:
            cards_1[card] = 1
    
    for card in hand2:
        if card in cards_2:
            cards_2[card] = 1 + cards_2[card]
        else:
            cards_2[card] = 1
                        
    if (len(cards_1) < len(cards_2)):
        return 1
    elif (len(cards_1) > len(cards_2)):
        return 0
    
    # print(hand1, "--", cards_1, hand2, "--", cards_2)
    
    # if we get here, both hands are similar
    vals = cards_1.values()
    vals2 = cards_2.values()
    if len(cards_1) == 2:
        if 4 in vals and 3 in vals2:
            return 1
        elif 3 in vals and 4 in vals2:
            return 0
    elif len(cards_1) == 3:
        if 3 in vals and 2 in vals2:
            return 1
        elif 2 in vals and 3 in vals2:
            return 0
    
    # if we get here, both hands are the same type
    for card1, card2 in zip(hand1, hand2):
        cmp = is_val_greater(card1, card2)
        if cmp != -1:
            return cmp

# returns 1 if val1 is greater and 0 if not
def is_val_greater_2(val1, val2):
    if global_vals_2[str(val1)] > global_vals_2[str(val2)]:
        return 1
    elif global_vals_2[str(val1)] < global_vals_2[str(val2)]:
        return 0
    return -1

# returns 1 if hand1 is greater and 0 if not
def winning_hand_2(hand1, hand2):
    cards_1 = dict()
    cards_2 = dict()
    
    for card in hand1:
        if card in cards_1:
            cards_1[card] = 1 + cards_1[card]
        else:
            cards_1[card] = 1
    
    for card in hand2:
        if card in cards_2:
            cards_2[card] = 1 + cards_2[card]
        else:
            cards_2[card] = 1
            
    if "J" in cards_1.keys():
        num_Js = cards_1["J"]
        
        if (num_Js != 5):
            cards_1.pop("J")
            
        max_val = max(cards_1, key=cards_1.get)
        cards_1[max_val] += num_Js
                        
    if "J" in cards_2.keys():
        num_Js = cards_2["J"]
        
        if (num_Js != 5):
            cards_2.pop("J")
            
        max_val = max(cards_2, key=cards_2.get)
        cards_2[max_val] += num_Js
           
    if (len(cards_1) < len(cards_2)):
        return 1
    elif (len(cards_1) > len(cards_2)):
        return 0
    
    # print(hand1, "--", cards_1, hand2, "--", cards_2)
    
    # if we get here, both hands are similar
    vals = cards_1.values()
    vals2 = cards_2.values()
    if len(cards_1) == 2:
        if 4 in vals and 3 in vals2:
            return 1
        elif 3 in vals and 4 in vals2:
            return 0
    elif len(cards_1) == 3:
        if 3 in vals and 2 in vals2:
            return 1
        elif 2 in vals and 3 in vals2:
            return 0
    
    # if we get here, both hands are the same type
    for card1, card2 in zip(hand1, hand2):
        cmp = is_val_greater_2(card1, card2)
        if cmp != -1:
            return cmp
    

def partA(input):
    print("Part A")
    
    sum = 0
    ordering = []
    
    for hand, val in input:
        
        # first add only
        if (len(ordering) == 0):
            ordering.append((hand,val))
            continue
        
        for i, (h, v) in enumerate(ordering):
            if winning_hand(hand, h) == 0:
                ordering.insert(i, (hand,val))
                break
            if i+1 == len(ordering):
                ordering.insert(len(ordering), (hand, val))
                break
                
    # print(ordering)
        
    for i, (hand, val) in enumerate(ordering):
        sum += (i+1)*val
    
    return sum

def partB(input):
    print("Part B")
    
    sum = 0
    ordering = []
    
    for hand, val in input:
        
        # first add only
        if (len(ordering) == 0):
            ordering.append((hand,val))
            continue
        
        for i, (h, v) in enumerate(ordering):
            if winning_hand_2(hand, h) == 0:
                ordering.insert(i, (hand,val))
                break
            if i+1 == len(ordering):
                ordering.insert(len(ordering), (hand, val))
                break
                
    # print(ordering)
        
    for i, (hand, val) in enumerate(ordering):
        sum += (i+1)*val
    
    return sum

def entry():
    print("2023:Day7")
    input = parseInput("day7_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2023, 7, SESSION_ID, USER_AGENT)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    # submit(2, ansB, 2023, 7, SESSION_ID, USER_AGENT)

if __name__=="__main__":
    entry()