"""Advent of Code 2022, Day: 22
Author: David Eyrich
Link: https://adventofcode.com/2022/day/22"""

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
    parsedInput = ''
    
    return parsedInput

def partA(input):
    print("Part A")
    return 0

def partB(input):
    print("Part B")
    return 0

def entry():
    print("2022:Day22")
    input = parseInput("day22_input.txt")
    
    # uncomment below to submit part A
    # ansA = partA(input)
    # print(ansA)
    # submit(1, ansA, 2022, 22)
    
    # uncomment below to submit part B
    # ansB = partB(input)
    # print(ansB)
    # submit(2, ansB, 2022, 22)

if __name__=="__main__":
    entry()