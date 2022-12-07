"""Advent of Code 2022, Day: 7
Author: David Eyrich
Link: https://adventofcode.com/2022/day/7"""

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
    
    dirs = {}
    parent_dirs = []
    cur_dir = ''
    
    for cmd in input:
        cmd_list = cmd.split(' ')
        if (cmd_list[0] == '$'):
            if (cmd_list[1] == "cd"):
                if (cur_dir is not ''):
                    parent_dirs.append(cur_dir)
                if (dirs.__contains__(cmd_list[2])):
                    # just pass through
                    cur_dir = cmd_list[2]
                else:
                    dirs.update(cmd_list[2], [])
                    cur_dir = cmd_list[2]
            elif (cmd_list[1] == "ls"):
                continue
        else:
            if (cmd_list[0] == )
                            
                    
    return 0

def partB(input):
    print("Part B")
    return 0

def entry():
    print("2022:Day7")
    input = parseInput("day7_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 7)
    
    # uncomment below to submit part B
    # ansB = partB(input)
    # print(ansB)
    # submit(2, ansB, 2022, 7)

if __name__=="__main__":
    entry()