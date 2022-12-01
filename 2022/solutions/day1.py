"""Advent of Code 2022, Day: 1
Author: David Eyrich
Link: https://adventofcode.com/2022/day/1"""

import re
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
    
    return parsedInput

def findMax(a, b):
    if (a > b):
        return a
    else:
        return b

def partA(input):
    print("Part A")
    
    maxSum = 0
    maxSum2 = 0
    maxSum3 = 0
    sum = 0
    
    for i in input:
        if (i != ''):
            sum += int(i)
        else:
            maxSum = findMax(maxSum, sum)
            sum = 0
    print(maxSum)
    
    return maxSum

def partB(input):
    print("Part B")
    
    maxSum = 0
    maxSum2 = 0
    maxSum3 = 0
    sum = 0
    
    for i in input:
        if (i != ''):
            sum += int(i)
        else:
            if (sum == findMax(maxSum, sum)):
                maxSum3 = maxSum2
                maxSum2 = maxSum
                maxSum = sum
            elif (sum == findMax(maxSum2, sum)):
                maxSum3 = maxSum2
                maxSum2 = sum
            elif (sum == findMax(maxSum3, sum)):
                maxSum3 = sum
            sum = 0
    print(maxSum, maxSum2, maxSum3)
    sum_of_max = maxSum+maxSum2+maxSum3
    print(sum_of_max)
    return sum_of_max

def entry():
    print("entry")
    input = parseInput("../input/day1_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    # submit(1, ansA, 2022, 1)
    
    # uncomment below to submit part B
    ansB = partB(input)
    # submit(2, ansB, 2022, 1)
    
if __name__=="__main__":
    entry()