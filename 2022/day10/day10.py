"""Advent of Code 2022, Day: 10
Author: David Eyrich
Link: https://adventofcode.com/2022/day/10"""

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

def partA(input):
    print("Part A")
    
    cycles = []
    signal_strength = 1
    
    for line in input:
        line_split = line.split(' ')
        
        if (len(line_split) == 1):
            cycles.append(0)
        else:
            cycles.append(0)
            cycles.append(int(line_split[1]))
    
    sum_of_strength = 0
    count = 1
    for cycle in cycles:
        signal_strength += cycle
        count+=1
        if (count == 20 or count == 60 or count == 100 or count == 140 or count == 180 or count == 220):
            sum_of_strength += signal_strength*count
            
    
    return sum_of_strength

def partB(input):
    print("Part B")
    
    cycles = []
    signal_strength = 1
    
    for line in input:
        line_split = line.split(' ')
        
        if (len(line_split) == 1):
            cycles.append(0)
        else:
            cycles.append(0)
            cycles.append(int(line_split[1]))
    
    count = 1
    picture = []
    line = 0
    sprite = [0,1,2]
    inSprite = False
    for cycle in cycles:
        pos = count-1
        
        if (count == 1):
            picture.append([])
        elif (count == 41 or count == 81 or count == 121 or count == 161 or count == 201):
            picture.append([])
            line += 1
            
        for s in sprite:
            if pos % 40 == s:
                picture[line].append('#')
                inSprite = True
        
        if (not inSprite):
            picture[line].append('.')
            
        signal_strength += cycle
        sprite[1] = signal_strength
        sprite[0] = sprite[1] - 1
        sprite[2] = sprite[1] + 1
        count+=1
        inSprite = False
        
        
    for line in picture:
        print(line)
    
    return 0

def entry():
    print("2022:Day10")
    input = parseInput("day10_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 10)
    
    # uncomment below to submit part B
    # For day 10, don't submit answer, just check the stdout.
    ansB = partB(input)
    print(ansB)
    # submit(2, ansB, 2022, 10)

if __name__=="__main__":
    entry()