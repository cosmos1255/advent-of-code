"""Advent of Code 2022, Day: 18
Author: David Eyrich
Link: https://adventofcode.com/2022/day/18"""

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
    input_lines = input.split('\n')
    parsedInput = []
    for line in input_lines:
        a,b,c = line.split(',')
        parsedInput.append((int(a), int(b), int(c)))
    
    return parsedInput

def partA(input):
    print("Part A")
    
    surface_area = 0
    for cube in input:
        temp_sa = 6
        
        # sides
        top = cube[0], cube[1], cube[2]+1
        bot = cube[0], cube[1], cube[2]-1
        left = cube[0]-1, cube[1], cube[2]
        right = cube[0]+1, cube[1], cube[2]
        front = cube[0], cube[1]-1, cube[2]
        back = cube[0], cube[1]+1, cube[2]
        
        for side in (top, bot, left, right, front, back):
            if (input.__contains__(side)):
                temp_sa -= 1
        surface_area += temp_sa
    
    return surface_area

def partB(input):
    print("Part B")
    
    return 0

def entry():
    print("2022:Day18")
    input = parseInput("day18_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    submit(1, ansA, 2022, 18)
    
    # uncomment below to submit part B
    # ansB = partB(input)
    # print(ansB)
    # submit(2, ansB, 2022, 18)

if __name__=="__main__":
    entry()