"""Advent of Code 2022, Day: 13
Author: David Eyrich
Link: https://adventofcode.com/2022/day/13"""

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
    parsedInput = ''
    
    return parsedInput

def partA(input):
    print("Part A")
    return 0

def partB(input):
    print("Part B")
    return 0

def entry():
    print("2022:Day13")
    input = parseInput("day13_input.txt")
    
    # uncomment below to submit part A
    # ansA = partA(input)
    # print(ansA)
    # submit(1, ansA, 2022, 13, SESSION_ID, USER_AGENT)
    
    # uncomment below to submit part B
    # ansB = partB(input)
    # print(ansB)
    # submit(2, ansB, 2022, 13, SESSION_ID, USER_AGENT)

if __name__=="__main__":
    entry()