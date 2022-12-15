"""Advent of Code 2022, Day: 8
Author: David Eyrich
Link: https://adventofcode.com/2022/day/8"""

import os
import sys
import re

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
    parsedInput = []
    for line in input.split('\n'):
        parsedInput.append(re.findall(r'\d', line))
    
    for i in range(len(parsedInput)):
        for j in range(len(parsedInput[0])):
            parsedInput[i][j] = int(parsedInput[i][j])
    
    return parsedInput

def partA(input):
    print("Part A")
    
    num_visible = 4 * len(input)-1
    counter = 0
    
    for i in range(1, len(input[1:-1])+1):
        for j in range(1, len(input[0][1:-1])+1):
            up = [input[i][j-k] for k in range(1, j+1)]
            down = [input[i][j+k] for k in range(1, len(input) - j)]
            left = [input[i-k][j] for k in range(1, i+1)]
            right = [input[i+k][j] for k in range(1, len(input) - i)]
        
            for d in (up, down, left, right):
                if (max(d) < input[i][j]):
                    num_visible += 1
                    break
    
    return num_visible

def partB(input):
    print("Part B")
    return 0

def entry():
    print("2022:Day8")
    input = parseInput("day8_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 8)
    
    # uncomment below to submit part B
    # ansB = partB(input)
    # print(ansB)
    # submit(2, ansB, 2022, 8)

if __name__=="__main__":
    entry()