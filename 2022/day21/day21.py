"""Advent of Code 2022, Day: 21
Author: David Eyrich
Link: https://adventofcode.com/2022/day/21"""

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
        input = f.read().splitlines()
        
    data = {}
    
    for line in input:
        val, operation = line.split(': ')
        operators = operation.split(' ')
        if (len(operators) == 1):
            data[val] = int(operators[0])
        else:
            data[val] = operators
            
    return data

def partA(input):
    print("Part A")
    
    arg_stack = []
    cur_val = "root"
    
    return 0

def partB(input):
    print("Part B")
    return 0

def entry():
    print("2022:Day21")
    input = parseInput("day21_input.txt")
    
    # uncomment below to submit part A
    # ansA = partA(input)
    # print(ansA)
    # submit(1, ansA, 2022, 21)
    
    # uncomment below to submit part B
    # ansB = partB(input)
    # print(ansB)
    # submit(2, ansB, 2022, 21)

if __name__=="__main__":
    entry()