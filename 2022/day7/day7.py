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

class LinkedList():
    def __init__(self, dir, val):
        self._dir = dir
        self._val = val
        self._children = {}
    
    def addChild(self, dir, val):
        self._children[dir] = LinkedList(dir, 0)
        
    def increaseSize(self, val):
        self._val += val

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
    level = 0
    parent_dirs = []
    cur_dir = ''
    cur_dir_size = 0
    
    for cmd in input:
        cmd_list = cmd.split(' ')
        if (cmd_list[0] == '$'):
            if (cmd_list[1] == "cd"):
                if (dirs == {}):
                    # should only enter here once
                    cur_dir = "MAIN_DIR"
                    dirs[cur_dir] = (0, {})
                    parent_dirs.append(cur_dir)
                else:
                    if (cmd_list[2] == ".."):
                        level -= 1
                        cur_dir = parent_dirs.pop()
                    else:
                        level += 1
                        parent_dirs.append(cur_dir)
                        cur_dir = cmd_list[2]
                    
                        cur_level = level
                        next_dir = dirs[parent_dirs[::-1][cur_level]]
                        while (cur_level > 0):
                            cur_level -= 1
                            next_dir = next_dir[1][parent_dirs[::-1][cur_level]]
                        next_dir[1][cmd_list[2]] = (0, {})
                        
                        
                        
            elif (cmd_list[1] == "ls"):
                continue
        else:
            if (cmd_list[0] == "dir"):
                cur_level = level
                next_dir = dirs[parent_dirs[::-1][cur_level]]
                while (cur_level > 0):
                    cur_level -= 1
                    next_dir = next_dir[1][parent_dirs[::-1][cur_level]]
                next_dir[1][cmd_list[1]] = (0, {})
                print(dirs)
                    
            
                
    # print(dirs)
    
    # find how many are under 100000 and add to sum
    # sum_of_vals = 0
    # for dir in dirs:
    #     vals = dir.values()
    #     for size in vals:
    #         if (size < 100000):
    #             sum_of_vals += size
         
    return sum_of_vals

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