"""Advent of Code 2023, Day: 4
Author: David Eyrich
Link: https://adventofcode.com/2023/day/4"""

import os
import sys
import re

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
    cards = input.split('\n')
    
    for i, card in enumerate(cards):
        cards[i] = card.split(': ')
        cards[i] = cards[i][1]
        cards[i] = cards[i].split(' | ')
        cards[i][0] = re.split(r'\s+', cards[i][0])
        cards[i][1] = re.split(r'\s+', cards[i][1])       
    
    return cards

def checkWinners(winning, reg_num):
    total = 0
    first = 1
    
    for winner in winning:
        if reg_num.__contains__(winner) and first:
            total = 1
            first = 0
        elif reg_num.__contains__(winner):
            total *= 2            
    
    return total

def numWinners(winning, reg_num):
    total = 0
    
    for winner in winning:
        if reg_num.__contains__(winner):
            total += 1
    
    return total

def partA(input):
    print("Part A")
    
    sum = 0
    
    for card in input:
        winning, reg_num = card
        
        sum += checkWinners(winning, reg_num)
            
    return sum

def partB(input):
    print("Part B")
    
    num_cards = [1]*len(input)
    
    for i, card in enumerate(input):
        winning, reg_num = card
        
        for j in range(num_cards[i]):
            for k in range(i+1, i+1+numWinners(winning, reg_num)):
                num_cards[k] += 1
            
    return sum(num_cards)

def entry():
    print("2023:Day4")
    input = parseInput("day4_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2023, 4, SESSION_ID, USER_AGENT)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    # submit(2, ansB, 2023, 4, SESSION_ID, USER_AGENT)

if __name__=="__main__":
    entry()