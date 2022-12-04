"""Advent of Code 2022, Day: 4
Author: David Eyrich
Link: https://adventofcode.com/2022/day/4"""

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
    pairs = input.split('\n')
    parsedInput = pairs
    
    return parsedInput

def isOverlapA(elf1, elf2):
    e1_a, e1_b = elf1.split('-')
    e2_a, e2_b = elf2.split('-')
    
    if (int(e1_a) >= int(e2_a) and int(e1_b) <= int(e2_b)):
        # print("overlaps")
        return 1
    elif (int(e2_a) >= int(e1_a) and int(e2_b) <= int(e1_b)):
        # print("overlaps")
        return 1
    else:
        # print("does not overlap")
        return 0
    
def isOverlapB(elf1, elf2):
    e1_a, e1_b = elf1.split('-')
    e2_a, e2_b = elf2.split('-')
    
    if (int(e1_a) <= int(e2_a) and int(e1_b) >= int(e2_a)):
        # print("overlaps")
        return 1
    elif (int(e1_a) <= int(e2_b) and int(e1_b) >= int(e2_b)):
        # print("overlaps")
        return 1
    elif (int(e2_a) <= int(e1_a) and int(e2_b) >= int(e1_a)):
        # print("overlaps")
        return 1
    elif (int(e2_a) <= int(e1_b) and int(e2_b) >= int(e1_b)):
        # print("overlaps")
        return 1
    # elif (int(e1_a) >= int(e2_a) and int(e1_b) <= int(e2_b)):
    #     # print("overlaps")
    #     return 1
    # elif (int(e2_a) >= int(e1_a) and int(e2_b) <= int(e1_b)):
    #     # print("overlaps")
    #     return 1
    else:
        # print("does not overlap")
        return 0

def partA(input):
    print("Part A")
    
    num_overlap = 0
    
    for pair in input:
        # print(pair)
        elf1, elf2 = pair.split(',')
        num_overlap += isOverlapA(elf1, elf2)
    
    # print(num_overlap)
        
    return num_overlap

def partB(input):
    print("Part B")
    
    num_overlap = 0
    
    for pair in input:
        # print(pair)
        elf1, elf2 = pair.split(',')
        num_overlap += isOverlapB(elf1, elf2)
    
    # print(num_overlap)
        
    return num_overlap

def entry():
    print("entry")
    input = parseInput("day4_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 4)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    submit(2, ansB, 2022, 4)

if __name__=="__main__":
    entry()