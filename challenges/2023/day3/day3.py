"""Advent of Code 2023, Day: 3
Author: David Eyrich
Link: https://adventofcode.com/2023/day/3"""

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
    parsedInput = input.split('\n')
    
    return parsedInput

def switch(symbols, i, j):
    if symbols.__contains__((i-1,j)):
        return 0
    if symbols.__contains__((i-1,j-1)):
        return 0
    if symbols.__contains__((i,j-1)):
        return 0
    if symbols.__contains__((i+1,j-1)):
        return 0
    if symbols.__contains__((i+1,j)):
        return 0
    if symbols.__contains__((i+1,j+1)):
        return 0
    if symbols.__contains__((i,j+1)):
        return 0
    if symbols.__contains__((i-1,j+1)):
        return 0
    return -1

def getNumbers(input, i, j):
    
    numbers = []
    for k in range(j-3, j+3):
        if input[i][k].isdigit():
            numbers.append(input[i][k])
        elif not input[i][k].isdigit() and k <= j:
            numbers = []
        elif not input[i][k].isdigit() and k > j:
            break
            
    return int(''.join(numbers))

def findAdjacent(input, numbers, i, j):
    adjacent = 0
    num_list = set()
    
    if numbers.__contains__((i-1,j)):
        adjacent += 1
        num_list.add(getNumbers(input, i-1, j))
    if numbers.__contains__((i-1,j-1)):
        adjacent += 1
        num_list.add(getNumbers(input, i-1, j-1))
    if numbers.__contains__((i,j-1)):
        adjacent += 1
        num_list.add(getNumbers(input, i, j-1))
    if numbers.__contains__((i+1,j-1)):
        adjacent += 1
        num_list.add(getNumbers(input, i+1, j-1))
    if numbers.__contains__((i+1,j)):
        adjacent += 1
        num_list.add(getNumbers(input, i+1, j))
    if numbers.__contains__((i+1,j+1)):
        adjacent += 1
        num_list.add(getNumbers(input, i+1, j+1))
    if numbers.__contains__((i,j+1)):
        adjacent += 1
        num_list.add(getNumbers(input, i, j+1))
    if numbers.__contains__((i-1,j+1)):
        adjacent += 1
        num_list.add(getNumbers(input, i-1, j+1))
        
        
    return num_list

def partA(input):
    print("Part A")
    
    sum = 0
    numbers = []
    symbols = []
    includeFlag = 0

    # find all of the symbols
    for i, line in enumerate(input):
        for j, ch in enumerate(line):
            if not ch.isdigit() and ch != '.': # we found symbols
                symbols.append((i,j))
                
    # print(symbols)
                
    # loop through all of the numbers and determine
    # if there are any symbols nearby
    for i, line in enumerate(input):
        for j, ch in enumerate(line):
            if ch.isdigit(): # we found symbols
                numbers.append(ch)
                if switch(symbols, i, j) == 0:
                    includeFlag = 1
            elif not ch.isdigit() and includeFlag: # number to be included
                sum += int(''.join(numbers))
                numbers = []
                includeFlag = 0 
                # print(sum)
            elif not ch.isdigit():
                numbers = []
    
    return sum

def partB(input):
    print("Part B")
    
    sum = 0
    numbers = []
    asterisks = []
    # includeFlag = 0

    # find all of the symbols
    for i, line in enumerate(input):
        for j, ch in enumerate(line):
            if ch == '*': # we found symbols
                asterisks.append((i,j))
            if ch.isdigit():
                numbers.append((i,j))
                
                
    for asterisk in asterisks:
        num_list = findAdjacent(input, numbers, asterisk[0], asterisk[1])
        if len(num_list) == 2:
            # print(num_list)
            sum += num_list.pop() * num_list.pop()
            
    return sum

def entry():
    print("2023:Day3")
    input = parseInput("day3_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2023, 3, SESSION_ID, USER_AGENT)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    submit(2, ansB, 2023, 3, SESSION_ID, USER_AGENT)

if __name__=="__main__":
    entry()