"""Advent of Code 2022, Day: 3
Author: David Eyrich
Link: https://adventofcode.com/2022/day/3"""

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

def getValA(s1, s2):
    for j in s1:
        for k in s2:
            if (j == k):
                if (ord(j) >= ord('A') and ord(j) <= ord('Z')):
                    return ord(j) - ord('A') + 27
                elif (ord(j) >= ord('a') and ord(j) <= ord('z')):
                    return ord(j) - ord('a') + 1
    print('did not get anything')
    return 0

def getValB(s1, s2, s3):
    for i in s1:
        for j in s2:
            for k in s3:
                if (i == j == k):
                    if (ord(j) >= ord('A') and ord(j) <= ord('Z')):
                        return ord(j) - ord('A') + 27
                    elif (ord(j) >= ord('a') and ord(j) <= ord('z')):
                        return ord(j) - ord('a') + 1
    print('did not get anything')
    return 0

def partA(input):
    print("Part A")
    
    sum = 0
    
    for i in input:
        s1 = i[0:int(len(i)/2)]
        s2 = i[int(len(i)/2):]
        sum += getValA(s1, s2)
        
    return sum

def partB(input):
    print("Part B")
    
    sum = 0
    
    l = len(input)
    
    for i in range(0, l, 3):
        sum += getValB(input[i], input[i+1], input[i+2])
    
    return sum

def entry():
    print("entry")
    input = parseInput("day3_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 3)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    # submit(2, ansB, 2022, 3)

if __name__=="__main__":
    entry()