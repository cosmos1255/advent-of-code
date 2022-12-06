"""Advent of Code 2022, Day: 2
Author: David Eyrich
Link: https://adventofcode.com/2022/day/2"""

import os
import sys

scripts_path = os.getcwd()
scripts_path_split = scripts_path.split('/')
scripts_path_join = '/'.join(scripts_path_split[:-2])
sys.path.append(f"{scripts_path_join}/scripts")

from submit_ans import submit

def parseInput(filename):
    # read in from a file
    with open(filename, 'r') as f:
        input = f.read()
        
    # parse through input here
    turns = input.split('\n')
    
    return turns

# rock = 1 = A = X
# paper = 2 = B = Y
# scissors = 3 = C = Z
# win = 6
# draw = 3
# loss = 0
# paper > rock : B > X or A < Y
# rock > scissors : A > Z or C < X
# scissors > paper : C > Y or B < Z
def checkScore(turn, part):
    outcomes_A = {'B X':1, 'A Z':3, 'C Y':2, 'A X':4, 'B Y':5, 'C Z':6, 'A Y':8, 'C X':7, 'B Z':9}
    outcomes_B = {'B X':1, 'A Z':8, 'C Y':6, 'A X':3, 'B Y':5, 'C Z':7, 'A Y':4, 'C X':2, 'B Z':9}
    
    if (part == 1):
        return outcomes_A[turn]
    elif (part == 2):
        return outcomes_B[turn]

def partA(input):
    print("Part A")
    
    myScore = 0
    
    for turn in input:
        myScore += checkScore(turn, 1) 
    
    return myScore

def partB(input):
    print("Part B")
    
    myScore = 0
    
    for turn in input:
        myScore += checkScore(turn, 2) 
    
    return myScore

def entry():
    print("2022:Day2")
    input = parseInput("day2_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 2)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    # submit(2, ansB, 2022, 2)

if __name__=="__main__":
    entry()