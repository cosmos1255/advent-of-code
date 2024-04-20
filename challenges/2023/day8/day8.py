"""Advent of Code 2023, Day: 8
Author: David Eyrich
Link: https://adventofcode.com/2023/day/8"""

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
    input = input.split("\n")
    
    dirs = input[0]
    ins = dict()
    
    for line in input[2:]:
        key, values = line.split(' = ')
        values = values.strip("()")
        
        ins[key] = values.split(", ")
    
    # print(dirs, ins)
    
    return dirs, ins

# input: (directions, instructions)
def partA(input):
    print("Part A")
    
    dirs, ins = input
    dir_i = 0
    
    cur = "AAA"
    
    while cur != "ZZZ":
        # print(cur)
        
        l,r = ins[cur]
        if dirs[dir_i % len(dirs)] == "L":
            cur = l
        else:
            cur = r
        
        dir_i += 1
        
    
    return dir_i

def end_with_z(cur_ins):
    for ins in cur_ins:
        if ins[2] != 'Z':
            return 0
        
    return 1

# input: (directions, instructions)
def partB(input):
    print("Part B")
    
    dirs, ins = input
    dir_i = 0
    
    ins_list = list()
    
    keys = ins.keys()
    
    for key in keys:
        if key[2] == 'A':
            ins_list.append(key)
            
    
    while not end_with_z(ins_list):
        
        for i, cur in enumerate(ins_list):
            l,r = ins[cur]
            if dirs[dir_i % len(dirs)] == "L":
                ins_list[i] = l
            else:
                ins_list[i] = r
        
        dir_i += 1
            
    
    return dir_i

def entry():
    print("2023:Day8")
    input = parseInput("day8_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2023, 8, SESSION_ID, USER_AGENT)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    # submit(2, ansB, 2023, 8, SESSION_ID, USER_AGENT)

if __name__=="__main__":
    entry()