"""Advent of Code 2022, Day: 20
Author: David Eyrich
Link: https://adventofcode.com/2022/day/20"""

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
    parsedInput = input.split('\n')
    
    for i, num in enumerate(parsedInput):
        parsedInput[i] = int(num)
    
    return parsedInput

def partA(input):
    print("Part A")
    
    length_in = len(input)
    
    for i, num in enumerate(input):
        print(input)
        new_index = (i + num) % length_in
        for i in range(new_index, length_in):
            temp = input[(new_index+1)%length_in]
            input[(new_index+1)%length_in] = input[new_index%length_in]
            
            if ():
                break
        input[new_index] = num
    
    a = input[(0+1000)%length_in]
    b = input[(0+2000)%length_in]
    c = input[(0+3000)%length_in]
    print(a, b, c)
    return a+b+c

def partB(input):
    print("Part B")
    return 0

def entry():
    print("2022:Day20")
    input = parseInput("day20_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 20)
    
    # uncomment below to submit part B
    # ansB = partB(input)
    # print(ansB)
    # submit(2, ansB, 2022, 20)

if __name__=="__main__":
    entry()