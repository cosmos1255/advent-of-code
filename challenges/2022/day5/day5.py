"""Advent of Code 2022, Day: 5
Author: David Eyrich
Link: https://adventofcode.com/2022/day/5"""

import os
import sys

scripts_path = os.getcwd()
scripts_path_split = scripts_path.split('/')
scripts_path_join = '/'.join(scripts_path_split[:-2])
sys.path.append(f"{scripts_path_join}/scripts")

from submit_ans import submit

def parseStacks(containers):
    container_rows = containers.split('\n')
    
    stacks = []
    
    for row in container_rows[::-1]:
        for i in range(1, len(row), 4):
            if (row[i].isalpha()):
                stacks[int(i / 4)].append(row[i])
            elif (row[i].isdigit()):
                stacks.append([])
                
    return stacks   

def parseCommands(commands):
    command_rows = commands.split('\n')
    cmds = []
    for cmd in command_rows:
        cmds.append(cmd.split(' '))
        
    return cmds

def parseInput(filename):
    # read in from a file
    with open(filename, 'r') as f:
        input = f.read()
        
    # parse through input here
    containers, commands = input.split('\n\n')
    stacks = parseStacks(containers)
    commands = parseCommands(commands)

    return stacks, commands

def partA(input):
    print("Part A")

    stacks, cmds = input

    m = 1
    f = 3
    t = 5
    
    for cmd in cmds:
        num_pops = int(cmd[m])
        # print(cmd)
        while (num_pops > 0):
            num_pops -= 1
            val = stacks[int(cmd[f])-1].pop()
            stacks[int(cmd[t])-1].append(val)
        # print(stacks)
        
    final_str = ""
    for stack in stacks:
        final_str += stack[-1]
        
    return final_str

def partB(input):
    print("Part B")
    
    stacks, cmds = input

    m = 1
    f = 3
    t = 5
    
    for cmd in cmds:
        num_pops = int(cmd[m])
        vals = []
        while (num_pops > 0):
            num_pops -= 1
            vals.append(stacks[int(cmd[f])-1].pop())
        for val in vals[::-1]:
            stacks[int(cmd[t])-1].append(val)
        
    final_str = ""
    for stack in stacks:
        final_str += stack[-1]
        
    return final_str

def entry():
    print("2022:Day5")
    input = parseInput("day5_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 5)
    
    input = parseInput("day5_input.txt")
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    # submit(2, ansB, 2022, 5)

if __name__=="__main__":
    entry()