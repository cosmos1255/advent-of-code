"""Advent of Code 2022, Day: 6
Author: David Eyrich
Link: https://adventofcode.com/2022/day/6"""

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
    
    return input

def noDuplicates(str):
    dupes = [0]*len(str)
    for ch in str:
        if (str.__contains__(ch)):
            dupes[str.index(ch)] += 1
    
    for val in dupes:
        if (val > 1):
            return False
    return True

def partA(input):
    print("Part A")
    
    str_len = len(input)
    
    for i in range(0, str_len-4):
        check_str = input[i:i+4]
        # print(check_str)
        if (noDuplicates(check_str)):
            return i+4
    return 0

def partB(input):
    print("Part B")
    
    str_len = len(input)
    
    for i in range(0, str_len-14):
        check_str = input[i:i+14]
        # print(check_str)
        if (noDuplicates(check_str)):
            return i+14
    return 0

def entry():
    print("2022:Day6")
    input = parseInput("day6_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 6)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    # submit(2, ansB, 2022, 6)

if __name__=="__main__":
    entry()